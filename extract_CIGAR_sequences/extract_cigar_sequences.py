############## @author: dewshrs@gmail.com ##################
############## This script is used to extract CIGAR tag specific sequences for Softclipped (S), matched (M), hardclipped (H), insertions (I) or mismatched (X) sequences ##################
############## This script is tested on python version 3.7. This will generate a fastq file based on selected CIGAR string. #################

import pandas as pd
import argparse
import sys
import re
from tqdm import tqdm

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input_sam_file', default=None, help = 'sam format file')
	parser.add_argument('-t','--cigar_tag', choices=['S','M','H', 'I','X'], default = 'S', help='cigar tag to be used to extract sequence')
	parser.add_argument('-l', '--length', default=19, type=int, help = 'minimum length of sequence to be extracted')
	parser.add_argument('-o', '--output_file', default = 'cigar_sequence.fq', help='output filename')

	args = parser.parse_args()

	return args




def main():
	args = arguments()

	if args.input_sam_file == None:
		print('\n!!! INPUT SAM FILE NOT PROVIDED !!! \n')
		sys.exit(1)

	sam_file = open(args.input_sam_file, 'r').readlines()

	
	with open(args.output_file, 'w') as f:
		for line in tqdm(sam_file):
			data = line.split('\t')
			cigar = data[5]
			sequence = data[9]
			read_quality = data[10].replace('\n','')

			m = re.findall(r"(\d+)M", cigar)
			s = re.findall(r"(\d+)S", cigar)
			h = re.findall(r"(\d+)H", cigar)
			i = re.findall(r"(\d+)I", cigar)
			x = re.findall(r"(\d+)x", cigar)

			indices_m = pd.DataFrame([[i.start() for i in re.finditer('M', cigar)],m]).transpose()
			indices_m['label'] = 'M'
			indices_s = pd.DataFrame([[i.start() for i in re.finditer('S', cigar)],s]).transpose()
			indices_s['label'] = 'S'
			indices_h = pd.DataFrame([[i.start() for i in re.finditer('H', cigar)],h]).transpose()
			indices_h['label'] = 'H'
			indices_i = pd.DataFrame([[i.start() for i in re.finditer('I', cigar)],i]).transpose()
			indices_i['label'] = 'I'
			indices_h = pd.DataFrame([[i.start() for i in re.finditer('X', cigar)],x]).transpose()
			indices_h['label'] = 'X'
		
			indices = pd.concat([indices_m,indices_s, indices_h])
			indices.columns = ['pos','len','label']
			indices = indices.sort_values('pos')

			n = 0


			for i in range(indices.shape[0]):
				if indices.iloc[i,2] == args.cigar_tag:
					length = n+int(indices.iloc[i,1])
					cigar_seq = sequence[n:length]
					if len(cigar_seq)> args.length:
						f.write(f"@CIGAR: '{args.cigar_tag}' SPECIFIC-SEQUENCE length={len(cigar_seq)}\n")
						f.write(cigar_seq)
						f.write('\n+\n')
						f.write(f"{read_quality[n:length]}\n")
						n = n+int(indices.iloc[i,1])
				else:
					n = n+int(indices.iloc[i,1])




if __name__ == '__main__':
	main()




