# IFDP

![](Figure1.svg)

The inferred fiber degradtion computational framework couples metagenomic sequencing with careful annotation of polysaccharide degrading enzymes and DFs structures has been established to allow the in-depth characterization of the microbiome ability to degrade and breakdown dietary fibers.

The simple framework allows to generate the Inferred Fiber Degradtion Profile (IFDP) in a single command necessitating the database (pre-built or re-built with a different version of diamond) fasta (or fastq) file. 

### Requirments:
- Diamond (database was built with v0.9.9, yet the database can be re-built using the database attached)
- Numpy
- Pandas

### Simple one command pipeline:

```./run_sample.sh [DATABASE] [INPUT] [OUTPUT]```

### Outputs:

[OUTPUT] - The diamond mapping output file

[OUTPUT]_counts - The enzyme counts

[OUTPUT]_IFDP - The IFDP profile name



### Tutorial

For easy testing of the framework,  we have uplaoded three Prevotella copri genomes (which are relatively small in size, memory and run time requirements) as simple use cases. To run any of the genomes just use this command, while changing the genome file name.

```./run_sample.sh ec_full.dmnd GCF_002075875.1_Bbif1898B_genomic.fna output```
