# IFDP

![](Figure1.svg)

The inferred fiber degradtion computational framework couples metagenomic sequencing with careful annotation of polysaccharide degrading enzymes and DFs structures has been established to allow the in-depth characterization of the microbiome ability to degrade and breakdown dietary fibers.

The simple framework allows to generate the Inferred Fiber Degradtion Profile (IFDP) in a single command necessitating the database (pre-built or re-built with a different version of diamond) fasta (or fastq) file. 

### Dependencies:
- Diamond (database was built with v0.9.9, yet the database can be re-built using the database attached)
- Numpy
- Pandas

### Installation

1.Install dependencies:
```conda install numpy pandas diamond ## install depandicies ```

2.Download the repo:
```git clone https://github.com/borenstein-lab/IFDP.git```

3.Extract the databaase and build it with diamond:
```gunzip ec_full.fasta.gz
diamond makedb --in ec_full.fasta.gz -d ec_full
```
4.Test the installation by running this example:
```./run_sample.sh ec_full.dmnd GCF_002075875.1_Bbif1898B_genomic.fna output```

5. run the pipeline using a simple one line command:

```./run_sample.sh [DATABASE] [INPUT] [OUTPUT]```

### Tutorial output and testing

For easy testing of the framework,  we have uplaoded three genomes (which are relatively small in size, memory and run time requirements) as simple use cases. To run any of the genomes just use this command, while changing the genome file name.

```./run_sample.sh ec_full.dmnd GCF_002075875.1_Bbif1898B_genomic.fna output```

In order to run and explore the results, a user must specify the database he wishes to use the input fasta/fastq file and an output name for the diamond output.

```./run_sample.sh [DATABASE] [INPUT] [OUTPUT]```

Three outputs will be visible following the completion of the run:

[OUTPUT] - The diamond mapping output file
<img width="998" alt="image" src="https://user-images.githubusercontent.com/33667593/195006139-0cdd5e34-288d-4a05-81ac-4f6606a75a00.png">

[OUTPUT]_counts - The enzyme counts
<img width="998" alt="image" src="https://user-images.githubusercontent.com/33667593/195006860-fdd941be-7c1d-4b0e-944d-d0963fb83c75.png">

[OUTPUT]_IFDP - The IFDP profile 
<img width="998" alt="image" src="https://user-images.githubusercontent.com/33667593/195006813-3d7dc26e-90cb-46cc-a1f4-5acb4e1bc2d3.png">


