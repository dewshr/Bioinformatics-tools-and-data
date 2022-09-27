# Running the program:
You can run the program simply by passing same length fasta sequences:

`python create_logo.py -i test_data/test.fa`

# Parameters:
```
python create_logo.py -h
usage: create_logo.py [-h] [-i INPUT_FASTA] [--out_name OUT_NAME] [-o OUTPUT_FOLDER]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FASTA, --input_fasta INPUT_FASTA
                        input fasta file
  --out_name OUT_NAME   output file name, default = result.png
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        output folder name, default=result
                        
```

# Output:
 This program generates the motif logo in `png` and `pdf` format along with the `pwm matrix`.
