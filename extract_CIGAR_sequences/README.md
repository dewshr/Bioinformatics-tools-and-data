## Extract CIGAR specific sequences from SAM file
The program **extract_cigar_sequences.py** takes [SAM](https://genome.sph.umich.edu/wiki/SAM) file as an input and based on the provided [CIGAR](https://replicongenetics.com/cigar-strings-explained/) strings, generates a fastq file.

### 1) Requirements
The program is tested on python 3.7.9. The user will require following packages:
  - pandas
  - tqdm

### 2) Input file
The program takes SAM file as an input. Sample file  `input.sam` generated using [STAR](https://github.com/alexdobin/STAR) is provided for test purpose.

### 3) Running the Program
The program can be run using `python extract_cigar_sequences.py -i input.sam -t S -o softclipped_reads.fq` -l 19. Here, `-i` takes input sam file, `-t` takes CIGAR strings, `-o` takes output file name and `-l` takes the length threshold to filter out the sequences which only extracts sequences greater than `l`. The full parameters available can be viewed by `python extract_cigar_sequences.py -h`

```
usage: extract_cigar_sequences.py [-h] [-i INPUT_SAM_FILE] [-t {S,M,H,I,X}]
                                  [-l LENGTH] [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_SAM_FILE, --input_sam_file INPUT_SAM_FILE
                        sam format file
  -t {S,M,H,I,X}, --cigar_tag {S,M,H,I,X}
                        cigar tag to be used to extract sequence
  -l LENGTH, --length LENGTH
                        minimum length of sequence to be extracted. Default: 19
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        output filename
```
