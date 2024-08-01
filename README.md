# E. coli BL21: Introduction
Our Lab loves E coli BL21! We are a group of people in science collectively using (and ab-using) E coli BL21 for several of its features which I'm going to summarize in the next section. 

## Table of Contents
1. [Overview](#overview)
2. [Genetic Features](#genetic-features)
    - [T7 RNA Polymerase and T7 Expression System](#t7-rna-polymerase-and-t7-expression-system)
    - [Lacking Lon and OmpT Proteases](#lacking-lon-and-ompt-proteases)
    - [Transformation Efficiency and Genetic Manipulation](#transformation-efficiency-and-genetic-manipulation)
    - [Growth Characteristics](#growth-characteristics)
3. [Applications](#applications)

## 1. Overview
E. coli strains like BL21(DE3) are used for recombinant RNA/protein expression due to their genetic features. These strains lack proteolytic activity and have a T7 RNA polymerase gene controlled by the lacUV5 promoter.

## 2. Genetic Features

### 2.1. T7 RNA Polymerase and T7 Expression System
1. BL21(DE3) carries the T7 RNA polymerase gene under the lacUV5 promoter's control.
2. Derived from E. coli B strains, BL21(DE3) carries the DE3 lysogen (a prophage) containing the T7 RNA polymerase gene.
3. T7 RNA polymerase is activated by IPTG, inducing high transcription rates of the target gene.
4. Expression system components:
   - T7 RNA polymerase downstream of IPTG-inducible lacUV5 promoter in the genome.
   - Expression vector with the transgene downstream of the T7 promoter.
   - T7 promoter is strong and tightly regulated, producing high levels of recombinant RNA/protein.
   - IPTG acts as an inducer, releasing repression on the lacUV5 promoter, thus controlling recombinant production timing and amount.
   - Specificity: T7 RNA polymerase selectively transcribes the target gene under the T7 promoter.
   - Versatility: Compatible with various T7 expression vectors for efficient protein expression.

### 2.2. Lacking Lon and OmpT Proteases
1. BL21 lacks Lon (cytoplasmic) and OmpT (outer membrane) proteases.
2. This ensures recombinant proteins are not degraded post-synthesis, allowing for efficient harvesting.

### 2.3. Transformation Efficiency and Genetic Manipulation
1. High transformation efficiency facilitates the incorporation of recombinant DNA constructs.
2. Amenable to various genetic manipulations for specific research needs.

### 2.4. Growth Characteristics
1. Rapid growth in standard bacterial media with a short doubling time (20-30 minutes).
2. Suitable for moderate to high yields of protein production, aiding in purification and downstream applications.
3. Widely used to express soluble proteins.
4. Compatible with various expression vectors, such as pET vectors, enhancing protein expression, purification, and detection.

## 3. Applications
E. coli BL21 is widely used strain in biotechnology and molecular biology due to its proficiency in protein expression. One of its primary applications is in the production of recombinant proteins, where its genetic modifications facilitate high-yield expression and simplified purification processes. As I mentioned before, E coli BL21 is "engineered" to lack proteases that can degrade expressed proteins, enhancing the stability and integrity of the products. It is also commonly utilized in the synthesis of enzymes, therapeutic proteins, and industrial biocatalysts. Additionally, its robust growth characteristics and well-understood genetics make it a valuable tool for research and development in various fields, including pharmaceuticals, agriculture, and bioengineering. E coli's compatibility with various expression vectors and its ability to perform post-translational modifications, albeit limited compared to eukaryotic systems, further expand its utility in the production of complex proteins.

# Statement of Problem
We have two mutated sequences of *E. coli* BL21, we call them OSB1 and OSB2. Our goal is to understand their exceptional export mechanism, in spite of accumulated mutations. Some questions we would like to answer are:

- What are the regions in which it acquired its mutations?
- Given the mutations they accumulated, what are the genes and their respective pathways that have a probability to affect processes like secretion and cellular export?
- Are there inserts that consist of duplicates of export genes?


# Installing & Using MAUVE for Genome Alignment

MAUVE is a multiple genome alignment tool that is hosted at the [Darling Lab](https://darlinglab.org/mauve/mauve.html) at the University of Technology Sydney. It is no longer maintained but remains to be freely available for users. A basic requirement for Mauve is Java version 1.4 or later (so, make sure Java is up and set to path!). Mauve is available for download on Windows, Linux, and Mac OS X 10.7+ at [Mauve's page](https://darlinglab.org/mauve/download.html). Follow through the instructions and it should be easy to set up Mauve.

Here's a summary of how I would usually do it on my Ubuntu 22.04 workstation:

1. MAUVE requires Java and other libraries to run. First, ensure you have Java installed:

    ```bash
    java -version
    ```

2. If not, install all the dependencies. I will provide the dirty installation here. You should go to [Oracle's Java website](https://www.oracle.com/java/technologies/downloads/?er=221886) and download one.

    ```bash
    sudo apt-get install default-jre
    sudo apt-get install default-jdk
    ```

3. Download, extract & run Mauve:

    There are two ways you can do this: one, download from the website and two, use 'wget' to download it directly from your terminal.

    **Way one:** Download a tarball from the Download page.

    **Way two:** Clone using wget:

    ```bash
    wget http://darlinglab.org/mauve/snapshots/latest/mauveSnapshot_2015-02-13_linux-x64.tar.gz
    ```

    Extract:

    ```bash
    tar -xvzf mauveSnapshot_2015-02-13_linux-x64.tar.gz
    ```

    Navigate to the Mauve directory:

    ```bash
    cd mauveSnapshot_2015-02-13
    ```

    Run:

    ```bash
    ./mauve
    ```
# Genome Alignment: Ecoli BL21 (Reference), OSB 1 and OSB 2

We use Mauve to align the three sequences, one being the reference sequence of *E. coli* BL21 downloaded from the NCBI. Based on the NCBI search hits, we choose to use the *E. coli* BL21 sequenced and submitted by New England Biolabs.

- Organism: *Escherichia coli*
- Infraspecific name: Strain: BL21
- Submitter: New England Biolabs
- Date: May 26, 2020
- Assembly level: Complete Genome
- Genome representation: full
- GenBank assembly accession: GCA_013166975.1
- RefSeq assembly accession: GCF_013166975.1


You should find a copy of OSB1 and OSB2 genomes in the repo itself. For reference purposes, the genome assembly file for *E. coli* BL21 full genome is copied into this repo. Check for the files [here](https://github.com/saysayani11/NGS_Ecoli_bl21/tree/main/1_sequences) and [here](https://github.com/saysayani11/NGS_Ecoli_bl21/tree/main/2_ncbi_dataset_full_genome). The fasta files would be all you need to build a basic alignment. Mauve creates 5 files: (a) A log (b) a .alignment that contains information on the aligned regions and unique regions that doesnt have any match (c) a .backbone file (d) a guide tree file and lastly, (e) A .islands file. We are going to use the .alignment and the .islands file.

 
# Gene Annotation & Transfer

Gene annotations were obtained using in-house Python codes to “map and transfer” annotations of *E. coli* BL21 (taken from the NCBI), which were then used as feed for genome alignment software “Mauve”. Information from the genome alignments generated from Mauve (Reference *E. coli* BL21, OSB1, and OSB2) were incorporated into the algorithm while mapping the genes onto the full genome sequences of OSB1 and OSB2. [Check the files here.](https://github.com/saysayani11/NGS_Ecoli_bl21/tree/main/4_annotation_transfer)

Consequently, we have a list of genes that were found to be exact matches onto the *E. coli* BL21 reference genome. The rest that did not were deemed as the genes that had accumulated mutations (hence, matches were not found). These mutations include mutations like frameshift, indels, SNPs. [Check the files here.](https://github.com/saysayani11/NGS_Ecoli_bl21/tree/main/4_annotation_transfer)

We use [DAVID Bioinformatics](https://david.ncifcrf.gov/tools.jsp) to find out associated pathways (GO) as well as a broader KEGG-based pathway annotations for the genes that were found mutated in OSB 1 and OSB 2. So, the final file comprises the following information:

- **Gene ID:** Gene ID refers to a unique identifier assigned to a gene.
- **Gene Name:** The gene name is a descriptive label given to a gene, usually indicating its function or a characteristic feature.
- **Pathways involved:** This refers to the specific biological pathways in which the gene is known to participate. Biological pathways are a series of actions among molecules in a cell that lead to a certain product or change in the cell, such as the glycolysis pathway or the TCA cycle.
- **KEGG based broader pathway classification:** KEGG (Kyoto Encyclopedia of Genes and Genomes) is a comprehensive database resource that provides information on the functions and utilities of the biological system. Broader pathway classification refers to the categorization of genes based on KEGG's detailed pathway maps, which include metabolism, genetic information processing, environmental information processing, and more.
- **Cellular localization:** Cellular localization describes the specific location within the cell where the gene product (usually a protein) is found. This can include locations such as the cytoplasm, nucleus, mitochondria, plasma membrane, or extracellular space.

Other notable information in the files include the GO identifiers (e.g., GO:0046942) that can be used to directly access a pathway’s respective information from the NCBI. Under the KEGG column, identifiers such as eco02010:ABC transporters redirect the KEGG page to the elaborate pathways that particular gene is involved in.

Our work is based on this data that comprises a list of genes (both in OSB1 and OSB2) holding mutations and are specifically involved in export, secretion, and are a part of membrane entities.[See the files here.](https://github.com/saysayani11/NGS_Ecoli_bl21/tree/main/6_mutations_in_secretory_pathway_proteins)

# Pseudocode for Transferring Annotations

## Define paths to the files

The files we will be using are the .alignment and the jsonl file from the NCBI-downloaded E coli BL21 assembly folder.
- Define `alignment_file_path`
- Define `jsonl_file_path`
- Define `output_file_path`

The alignment file has a unique, neat format. It's contents are formatted into "alignment blocks" that (typically) starts with a ">" and end with a "=". Headers of each alignment blocks give information about the sequence, the orientation of alignment (+/-), and the region (start, stop in basepairs) of alignment.

Towards the end of the alignment file, (approximately line number 170791, if youre using text editor in Ubuntu 22), lists the (sub)sequences that do not have a corresponding alignment to it. These are of particular importance to us because this gives information on the "extras" of OSB 1 and OSB 2. For now, we will parse the alignment file in the following function:

## Function to read and parse the alignment file
Open file at `file_path` for reading:
    For each line in file:
        If line matches `block_pattern`:
            If `current_block` exists:
                Append `current_block` to `blocks`
            Initialize `current_block` with matched data
        Else if `current_block` exists:
            Append line to `current_block`'s sequence
    
    If `current_block` exists:
        Append `current_block` to `blocks`

Return `blocks`

Where do we pick the genome annotations from? There may be several ways, but for simplicity, we turn back to out genome assembly file for E coli BL21 from NCBI. 
## Function to parse the JSONL file and extract gene coordinates

Open file at `file_path` for reading:
    For each line in file:
        Parse line as JSON to `gene_data`
        For each region in `gene_data.genomicRegions`:
            Extract and normalize gene information
            Append gene information to `genes`

Return `genes`


## Function to map alignment blocks to genes


For each block in `blocks`:
    Find overlapping genes in `genes_df`
    Append block and corresponding genes to `mapped_genes`

Return `mapped_genes`


## Parse the alignment file
- Call `parse_alignment_file` with `alignment_file_path` to get `alignment_blocks`
- Print the number of parsed alignment blocks

## Parse the JSONL file
- Call `parse_jsonl` with `jsonl_file_path` to get `genes_data`
- Print the number of parsed genes

## Convert genes data to a DataFrame
- Convert `genes_data` to DataFrame `genes_df`
- Print the head of `genes_df`

## Map alignment blocks to genes
- Call `map_blocks_to_genes` with `alignment_blocks` and `genes_df` to get `mapped_genes`
- Print the number of mapped blocks to genes

## Save the results to a CSV file

## Group by sequence and identify unique genes
- Group `mapped_genes_df` by `Gene_Seqname` and get unique `Gene_Symbol` for each group
- Save the unique genes for each sequence to `unique_genes_per_sequence.csv`

- Print the output file path for the unique genes per sequence
