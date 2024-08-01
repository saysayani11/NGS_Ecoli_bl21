# E. coli BL21: Introduction

## Table of Contents
1. [Overview](#overview)
2. [Genetic Features](#genetic-features)
    - [T7 RNA Polymerase and T7 Expression System](#t7-rna-polymerase-and-t7-expression-system)
    - [Lacking Lon and OmpT Proteases](#lacking-lon-and-ompt-proteases)
    - [Transformation Efficiency and Genetic Manipulation](#transformation-efficiency-and-genetic-manipulation)
    - [Growth Characteristics](#growth-characteristics)
3. [Applications](#applications)

## 1. Overview
E. coli strains like BL21(DE3) and DL39 are used for recombinant RNA/protein expression due to their genetic features. These strains lack proteolytic activity and have a T7 RNA polymerase gene controlled by the lacUV5 promoter.

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
1. High yield production of recombinant proteins for structural studies, biochemical analyses, and initial protein characterization.

# Statement of Problem

# Gene Annotation Transfer

# Installing & Using MAUVE for Genome Alignment

MAUVE is a multiple genome alignment tool that is hosted at the [Darling Lab](https://darlinglab.org/mauve/mauve.html) at the University of Technology Sydney. It is no longer maintained but remains freely available for users. A basic requirement for Mauve is Java version 1.4 or later (so, make sure Java is up and set to path!). Mauve is available for download on Windows, Linux and Lac OS X 10.7+ at [Mauve's page](https://darlinglab.org/mauve/download.html). Follow through the instructions and it should be easy to set up Mauve. 

Here's a sumamry of how I would usually do it on my Ubuntu 22.04 workstation: 

1. MAUVE requires Java and other libraries to run. First, ensure you have Java installed:
java -version

2. If no, install all the dependencies. I will provide the dirty installion here. You should go to ]Oracle's Java website](https://www.oracle.com/java/technologies/downloads/?er=221886) and download one.
   
sudo apt-get install default-jre
sudo apt-get install default-jdk

3. Download, extract & run Mauve

There are two ways you can do this: one, download from the website and two, use 'wget' to download it directly.
Way one: Download a tarball from the Download page.
Way two: Clone: wget http://darlinglab.org/mauve/snapshots/latest/mauveSnapshot_2015-02-13_linux-x64.tar.gz

Extract: tar -xvzf mauveSnapshot_2015-02-13_linux-x64.tar.gz
Navigate to the Mauve directory: cd mauveSnapshot_2015-02-13
Run: ./mauve



