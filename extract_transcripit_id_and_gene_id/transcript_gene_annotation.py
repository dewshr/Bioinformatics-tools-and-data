############## @author: dewshrs@gmail.com ##################
############## This script is used to extract corresponding trancript and id and gene id from the gtf file ##################
import argparse
import sys


def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--gtf_file', default=None, help = 'gtf file to be used for transcript gene annotation file creation')
	parser.add_argument('--gene_version', action = 'store_true', help='use gene version')
	parser.add_argument('--gtf_source', choices=['gencode', 'ensembl'], default = 'gencode', help = 'gtf file source information. Depending on the source, information are stored slightly different. By default it uses gencode')
	parser.add_argument('-o','--output_file', default='transcript_annotation.txt', help='output filename')

	args = parser.parse_args()

	return args

def create_annotation_gencode(gtf_file, gene_version_bool):
	annotation_dict = {}
	for line in gtf_file:
		if line.startswith('#'):
			continue
		if line.split('\t')[2] == 'transcript':
			#data = line.split(';')
			
			gene_id = line.split('gene_id "')[1].split('"')[0]
			transcript_id = line.split('transcript_id "')[1].split('"')[0]
			gene_name = line.split('gene_name "')[1].split('"')[0]

			if gene_version_bool == True:
				annotation_dict[transcript_id] = [gene_id, gene_name]
			else:
				annotation_dict[transcript_id] = [gene_id.split('.')[0], gene_name]


	return annotation_dict


def create_annotation_ensembl(gtf_file, gene_version_bool):
	annotation_dict = {}
	for line in gtf_file:
		if line.startswith('#'):
			continue
		if line.split('\t')[2] == 'transcript':
			data = line.split(';')
			
			gene = data[0].split(' "')[1].strip('"')
			gene_version = data[1].split(' "')[1].strip('"')

			transcript = data[2].split(' "')[1].strip('"')
			transcript_id = transcript + '.' + data[3].split(' "')[1].strip('"')

			gene_name = data[4].split(' "')[1].strip('"')

			if gene_version_bool == True:
				gene_id = gene + '.' + gene_version
				annotation_dict[transcript_id] = [gene_id, gene_name]
			else:
				annotation_dict[transcript_id] = [gene, gene_name]


	return annotation_dict
			


def main():
	args = arguments()
	
	if args.gtf_file == None:
		print('\n!!!! GTF file not provided !!!!! \n')
		sys.exit(1)

	gtf_file = open(args.gtf_file,'r').readlines()

	if args.gtf_source == 'gencode':
		annotation = create_annotation_gencode(gtf_file, args.gene_version)
	elif args.gtf_source == 'ensembl':
		annotation = create_annotation_ensembl(gtf_file, args.gene_version)
	else:
		print('invalid gtf source')
		sys.exit(1)

	with open(args.output_file, 'w') as f:
		f.write(f"ensembl_id\tensembl_gene\tgene_name\n")
		for key, value in annotation.items():
			f.write(f"{key}\t{value[0]}\t{value[1]}\n")


if __name__ == '__main__':
	main()
	








