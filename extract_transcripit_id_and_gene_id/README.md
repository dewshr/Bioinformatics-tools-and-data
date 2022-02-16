## Generate Transcript-Gene Annotation File
The program .py uses GTF file as input and extracts transcript id, ensembl gene id and gene name. 

### 1) Input file
The program takes GTF files as input. It can be downloaded from [Gencode](https://www.gencodegenes.org/human/release_19.html) or from [ensembl](https://useast.ensembl.org/info/data/ftp/index.html)
The annotation file uploaded here is downloaded from [here](http://ftp.ensembl.org/pub/grch37/release-105/gtf/homo_sapiens/).

### 2) Running the Program

The program can be run using `transcripts_to_gene.py -i Homo_sapiens.GRCh37.87.gtf --gene_version -o Homo_sapiens.GRCh37.87.t2g.txt --gtf_source ensembl`.
Since, depending on the ensembl or gencode, the version information are stored differently, so gtf_source should be provided. By default it assumes the source as **gencode**.
The parameter 'gene_version' adds gene version in the annotation file genetated. To see all the parameters available you can run `python get_gene_aliases.py -h`, which will give following details:

```
usage: transcripts_to_gene.py [-h] [-i GTF_FILE] [--gene_version]
                              [--gtf_source {gencode,ensembl}]
                              [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -i GTF_FILE, --gtf_file GTF_FILE
                        gtf file to be used for transcript gene annotation
                        file creation
  --gene_version        use gene version
  --gtf_source {gencode,ensembl}
                        gtf file source information. Depending on the source,
                        version information are stored differently. By default
                        it uses gencode
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        output filename
```
