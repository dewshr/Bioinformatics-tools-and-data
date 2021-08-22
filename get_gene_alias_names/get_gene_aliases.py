############## @author: dewshrs@gmail.com ##################
############## This script is used to extract the gene aliases from GeneCards Database. It can take single gene as a input or multiple genes in a text file ##########

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import argparse
from tqdm import tqdm
from joblib import Parallel, delayed


# program arguments
def prog_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input_gene', default =  None, help='single gene name')
	parser.add_argument('-b', '--batch_file', default =  None, help='text file with gene names')
	parser.add_argument('-n', '--num_core', type=int, default=2, help='NUmber of cores to run the program. Default is 2')

	args = parser.parse_args()

	return args

# function to get gene aliases name
def get_aliases(gene):
	url = 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=' + gene
	try:
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		response = urlopen(req).read()

		soup = BeautifulSoup(response, 'lxml')
		results = soup.find_all(itemprop='alternateName')
		aliases = []
		for val in list(results):
			aliases.append(str(val).split('">')[1].split('<')[0])

		if len(aliases) ==0:
			return '--'
		else:
			return ','.join(aliases)
	except:
		return '--'


def main():
	args = prog_args()

	if args.input_gene == None and args.batch_file ==  None:
		print("!!! Error: Didn't get any input")
		sys.exit()


	if args.input_gene != None:
		print(f"The aliases for {args.input_gene} are: {get_aliases(args.input_gene)}")


	if args.batch_file != None:
		genes = open(args.batch_file, 'r').read().split('\n')

		print("\n---- Retrieving gene aliases from GeneCards ----\n")

		all_aliases = Parallel(n_jobs=args.num_core)(delayed(get_aliases)(genes[i]) for i in tqdm(range(len(genes))))

		print("\n--------- Writing the results to file ----------\n")

		with open('genes_with_alias.txt','w') as f:
			for i in range(len(all_aliases)):
				f.write(f"{genes[i]}\t{all_aliases[i]}\n")


		print("\n\t\t !!! DONE !!! \t\t\n")


if __name__ == "__main__":
	main()

