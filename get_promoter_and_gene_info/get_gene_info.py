import pandas as pd
import sys


fname = sys.argv[1] # gtf file (https://www.gencodegenes.org/human/)
outname = fname.split('.gtf')[0]


df = pd.read_csv(fname, skiprows=5,sep='\t')
df.columns = ['chr','source','type','start','stop','val1','strand','val2','info']

df = df[df['type'] == 'gene']
df['gene'] = df['info'].apply(lambda x : x.split('gene_name "')[1].split('";')[0])
df['ensembl_gene'] = df['info'].apply(lambda x: x.split('gene_id "')[1].split('";')[0])

gene = df.loc[:,['chr','start','stop','gene','ensembl_gene','strand']]
gene = gene.drop_duplicates()
gene = gene.sort_values(['chr','start'])


gene.to_csv(f'{outname}.gene_info.bed', sep='\t', index=False, header=False)
