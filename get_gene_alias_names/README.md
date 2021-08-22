## Get Gene Aliases
The program extract the gene aliases name from [GeneCards](https://www.genecards.org/). It can take a single gene as a input or multiple genes in a text file as a batch input.
<br/>

# Contents

- [Prerequisites](#1-prerequisites)
- [Input file format](#2-input-file-format)
- [Running the program](#3-running-the-program)
- [Data Description](#4-data-description)
<br/>

## 1) Prerequisites

The program is tested on ***python 3.7*** using following packages:

- beautifulsoup4 = 4.8.1
- urllib3 = 1.25.7
- tqdm = 4.38.0
- joblib = 0.14.0

<br/>

## 2) Input file format

User can pass single gene as well as multiple genes. For multiple genes, gene names has to be passed as a text file with one gene in each line.

<br/>

## 3) Running the program

The simplest way to run the program is `python get_gene_aliases.py -i gene_name`. For batch run `python get_gene_aliases.py -b genes_filename`. To see all the parameters available you can run `python get_gene_aliases.py -h`, which will give following details:
```
usage: get_gene_aliases.py [-h] [-i INPUT_GENE] [-b BATCH_FILE] [-n NUM_CORE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_GENE, --input_gene INPUT_GENE
                        single gene name
  -b BATCH_FILE, --batch_file BATCH_FILE
                        text file with gene names
  -n NUM_CORE, --num_core NUM_CORE
                        NUmber of cores to run the program. Default is 2
```
For parallel processing in batch file you can pass the number of cores to be used through `-n` parameter.

<br/>

## 4) Data Description

- **biomart_hg38_ensembl_104_genes.txt :** This file contains list of all genes downloaded from [Biomart](https://m.ensembl.org/biomart/martview/b2de93a4c9540e93b7ae72a0649a1497) for **GRCh38.p13** using **Ensembl Genes 104** database.
- **genes_with_alias.txt :** This file contains all the aliases name found for the genes in `biomart_hg38_ensembl_104_genes.txt`. The file is tab delimited format with two columns. First column is the query **gene name** and second column name contains all the **aliases** separated by **","**. If aliases is not found, it is represented by **--**.
