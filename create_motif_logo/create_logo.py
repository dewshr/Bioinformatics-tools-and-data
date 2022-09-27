import logomaker
import pandas as pd
from Bio.Seq import Seq
from Bio import motifs
import argparse
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns


def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input_fasta', default =None, help='input fasta file')
	parser.add_argument('--out_name', default='result.png', help='output file name, default = result.png')
	parser.add_argument('-o','--output_folder', default ='result', help='output folder name, default=result')

	return parser





def main():
	parser = arguments()
	args = parser.parse_args()

	if not os.path.exists(args.output_folder):
		os.makedirs(args.output_folder)

	if args.input_fasta == None:
		print('\n\n !!!!!!! No input file provided. Exiting...!!!!!!\n\n')
		parser.print_help()
		sys.exit(1)


	name = (args.out_name).split('.')[0]

	print('..... Please make sure all the fasta sequences are of same length .....\n')
	
	print('.... reading in fasta file .....\n')
	fasta = open(args.input_fasta,'r').readlines()

	

	seq_list = []

	for line in fasta:
		if not line.startswith('>'):
			seq_list.append(line.upper().replace('\n',''))

	print('...... getting base counts .....\n')
	instances = [Seq(x.upper()) for x in seq_list]
	m = motifs.create(instances)

	m_df = pd.DataFrame(m.counts)

	print('..... creating information matrix for motif logo .....\n')
	t_df = logomaker.transform_matrix(m_df, from_type = 'counts', to_type='information')
	t_pwm = logomaker.transform_matrix(m_df, from_type = 'counts', to_type='probability')

	
	with open(f'{args.output_folder}/{name}.pwm','w') as f:
		f.write('MEME version 4\n\nALPHABET= ACGT\n\nstrands: + -\n\nBackground letter frequencies\nA 0.25 C 0.25 G 0.25 T 0.2\n\n')
		f.write(f'MOTIF {name} {name}_motif\nletter-probability matrix: alength= 4 w= {t_df.shape[0]} nsites= {len(seq_list)} E= 0\n')
		for i in range(t_df.shape[0]):
			f.write(f' {t_df.iloc[i,0]} {t_df.iloc[i,1]} {t_df.iloc[i,2]} {t_df.iloc[i,3]}\n')


	print('...... generating logo ......\n')
	sns.set(font_scale=1.5, style='white')
	plt.figure(figsize=(15,15))
	crp_logo=logomaker.Logo(t_df,font_name='Arial Rounded MT Bold')
	crp_logo.style_spines(visible=False)
	crp_logo.style_xticks(anchor=0)
	crp_logo.style_spines(spines=['left', 'bottom'], visible=True)

	plt.title(name)
	plt.tight_layout()
	plt.savefig(f"{args.output_folder}/{name}.png")
	plt.savefig(f"{args.output_folder}/{name}.pdf")


if __name__ == "__main__":
	main()




