# Bioinformatics Gene Annotation Comparison
### By Lily Hofman and Alex Habegger
This repository contains a bioinformatics software system that compares gene annotations between two releases for a chosen species. The system includes Python classes for data processing and information extraction, a MySQL relational database, and web-based interfaces for querying data on demand.

## Objectives

The project aims to answer the following questions:

1. How many different categories of genes (e.g., protein-coding, miRNA, and other non-coding genes) and their numbers exist in each release?
2. How many transcripts are annotated?
3. What are the associated transcript numbers for each gene category?
4. What are the maximum/minimum numbers of different transcripts annotated for a single gene?
5. Can you detect any detailed differences (e.g., different gene length, start/end positions, or different transcript numbers within a gene) between two releases for the same genes annotated?
6. What are the genes and transcripts annotated in one release but not in the other?

Additionally, the web interface allows users to search for a gene name and display the gene annotation information (e.g., chromosome, strand, start and end, gene category), as well as the relevant transcript annotation information (e.g., their start/end positions, number of exons and introns), from both releases for the selected gene.

## Getting Started

### Prerequisites

To run this project, you will need:

1. A MySQL database
2. A live server

### Installation

1. Download the following SQL files: `GeneCategories.sql`, `ReleaseInfo.sql`, `Transcripts100.sql`, `Transcripts104.sql`.
2. Execute the four SQL files in a database.
3. Download `index.html`, `GeneCompare.py`, and `ReleaseCompare.py` from the provided links.
4. Update `GeneCompare.py` and `ReleaseCompare.py` to connect to the database you set up in step two.
5. Place the three files downloaded in step three in a live server.
6. Run the following commands to set permissions:

   ```
   chmod a+rwx GeneCompare.py
   chmod a+rwx ReleaseCompare.py
   ```

## Usage

With the project set up, you can now use the web interface to search for gene names and retrieve gene annotation information from both releases for the selected gene. The interface also provides summary information (e.g., total number of annotated genes and transcripts, different gene categories, and relevant gene and transcript numbers) for both releases.

## Acknowledgments

* The Ensembl project for providing gene annotation data.
