# CSE 466 Final Project

_Alex Habegger and Lily Hofman_

**Objectives:**
The final project is designed to apply what you have learned in this course to solve real bioinformatics problems. In this
project, you will build a bioinformatics software system, which includes:
(1) python classes for data processing and information extraction, 
(2) a relational database implemented in MySQL that contains at least one table, and 
(3) web-based interfaces that can communicate with the database and allow users to query data on demand.

**Assignment:**
(1) Gene Annotation Comparison.
As we are making good progresses in sequencing more RNAs (i.e., more evidence of expressed genes), gap-filling
chromosomes (e.g., sequencing longer DNA fragments), and developing better genome annotation algorithms, the gene
annotations for different organisms are getting more and more accurate as time passes by. The major goal of this project
is to compare the gene annotations between two releases for your desired species. For example, we want to know gene
annotation differences for mouse genome between ENSEMBL release 103 (http://ftp.ensembl.org/pub/release-103/gtf/mus_musculus/Mus_musculus.GRCm39.103.chr.gtf.gz , released in Dec-25-2020) and release 104
(http://ftp.ensembl.org/pub/release-104/gtf/mus_musculus/Mus_musculus.GRCm39.104.chr.gtf.gz , released in Mar-16-
2021). Of course, you can choose other species you like. Through this project, you need to answer the following
questions. How many different categories of genes (e.g., protein-coding, miRNA and other non-coding genes) and their
numbers. How many transcripts are annotated? What are the associated transcript numbers for each gene category?
What are the maximum/minimum numbers of different transcripts annotated for a single gene? After comparing two
releases, you can tell us the differences between two releases regarding the above questions. Furthermore, for the same 
genes annotated in both releases, can you detect any detailed differences (e.g., different gene length, start/end positions,
or different transcript numbers within a gene)? What are the genes and transcripts annotated in the 104 release not in
the 103 release? What are genes and transcripts annotated in the 103 release not in the 104 release? Of course, you can
examine other questions that interest you! If a user queries your database through your web interface, you need to
allow the user to search gene name and display the gene annotation information (e.g., chromosome, strand, start and
end, gene category), as well as the relevant transcript annotation information (e.g., their start/end positions and how
many exons and introns), from both releases for the selected gene. Your interface also needs to show summary
information (e.g., total number of annotated genes and transcripts, as well as different gene categories and relevant gene
and transcript numbers) for both releases.
