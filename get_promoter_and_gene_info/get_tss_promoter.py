import pandas as pd
import sys

def get_tss(x):
	strand = x['strand']
	if strand == '+':
		return x['tss_s']
	else:
		return x['tss_e']

def get_promoter_start(x,n):
	strand = x['strand']
	if strand == '+':
		p1 = x['tss']-n
		if p1 < 0:
			p1=0
		return pd.Series([p1, x['tss']])
	else:
		return pd.Series([x['tss'], x['tss']+n])


fname = sys.argv[1] #gtf file (https://www.gencodegenes.org/human/)
outname = fname.split('.gtf')[0]

df = pd.read_csv(fname, skiprows=5,sep='\t')
df.columns = ['chr','source','type','tss_s','tss_e','val1','strand','val2','info']

df = df[df['type'] == 'transcript']
df['gene'] = df['info'].apply(lambda x : x.split('gene_name "')[1].split('";')[0])
df['ensembl_gene'] = df['info'].apply(lambda x: x.split('gene_id "')[1].split('";')[0])
df['tss'] = df.apply(lambda x: get_tss(x), axis=1)

tss = df.loc[:,['chr','tss','strand','gene','ensembl_gene']]
tss = tss.drop_duplicates()
tss = tss.sort_values(['chr','tss'])

tss[['p_start_1000', 'p_end_1000']] = tss.apply(lambda x: get_promoter_start(x, 1000), axis=1)
tss[['p_start_1500', 'p_end_1500']] = tss.apply(lambda x: get_promoter_start(x, 1500), axis=1)

tss.loc[:,['chr','p_start_1000','p_end_1000','gene','ensembl_gene','strand']].to_csv(f'{outname}_1000_promoter.bed', index=False, header=False, sep='\t')
tss.loc[:,['chr','p_start_1500','p_end_1500','gene','ensembl_gene','strand']].to_csv(f'{outname}_1500_promoter.bed', index=False, header=False, sep='\t')

tss.to_csv(f'{outname}.tss.bed', sep='\t', index=False, header=False)
