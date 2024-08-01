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

    There are two ways you can do this: one, download from the website and two, use 'wget' to download it directly.

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

# Algorithm for annotation transfer

