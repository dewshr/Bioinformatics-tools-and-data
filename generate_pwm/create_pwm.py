import pandas as pd
from Bio import motifs
from Bio.Seq import Seq
import logomaker
import argparse
import matplotlib.pyplot as plt
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--fasta', default=None, help='fasta sequence file')
parser.add_argument('-o','--output_name', default='custom_pwm', help='output file name')
parser.add_argument('-d','--dir', default='custom_pwm', help='output file directory')

args = parser.parse_args()

if not os.path.exists(args.dir):
	os.makedirs(args.dir)
if args.fasta == None:
	print('No input provided')
	sys.exit()
fasta = list(filter(None, open(args.fasta,'r').read().split('\n')))

l = len(fasta)/2.0
sequence_list = []

for i in range(1,len(fasta),2):
    sequence_list.append(Seq(fasta[i].upper()))

m = motifs.create(sequence_list)

pfm_df = pd.DataFrame(m.counts)
ppm_df = round(pfm_df/l,4)

with open(f"{args.dir}/{args.output_name}.meme",'w') as w:
	w.write(f'MEME version 4\n\nALPHABET= ACGT\n\nstrands: +-\n\nBackground letter frequencies\nA 0.25 C 0.25 G 0.25 T 0.25\n\nMOTIF {args.output_name} {args.output_name}\nletter-probability matrix: alength=4 w= {ppm_df.shape[0]} nsites={int(l)}\n')
	for i in range(ppm_df.shape[0]):
		w.write(f" {ppm_df.iloc[i,0]} {ppm_df.iloc[i,1]} {ppm_df.iloc[i,2]} {ppm_df.iloc[i,3]}\n")

crp_logo = logomaker.Logo(ppm_df,stack_order='big_on_top', font_name='Arial Rounded MT Bold')
crp_logo.style_spines(visible=False)
crp_logo.style_spines(spines=['left', 'bottom'], visible=True)

plt.title(args.output_name,fontsize=20)
plt.savefig(f"{args.dir}/{args.output_name}.pdf")
