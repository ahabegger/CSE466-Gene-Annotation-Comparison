

f = open("sqlQueries.txt", "w")



# FOR THE TRANSCRIPTS104 TABLE

FH = open("Danio_rerio.GRCz11.104.chromosome.12.gff3", 'r')

transcript_set = set()
dict = dict()

f.write("CREATE TABLE `Transcripts104` (`Chromosome` int(60) DEFAULT NULL,`Annotation_Provider` varchar(60) DEFAULT NULL,`Type` varchar(60) DEFAULT NULL,`Start_Position` int(60) DEFAULT NULL,`End_Position` int(60) DEFAULT NULL,`Dots` varchar(60) DEFAULT NULL,`Dash` varchar(60) DEFAULT NULL,`Number` varchar(60) DEFAULT NULL,`Transcript_ID` varchar(1000) DEFAULT NULL);")

for i in FH:
    if not i.startswith('#'):
        line = i.strip().split('\t')
        if line[2] not in dict.keys():
            dict[str(line[2])] = 1
        else:
            dict[str(line[2])] += 1
        if len(line) == 9:
            if "transcript:ENSDART" in line[8]:
                line[8] = line[8][line[8].find("transcript:ENSDART")+11:line[8].find("transcript:ENSDART")+29]
                transcript_set.add(line[8])
            if "gene:ENSDAR" in line[8]:
                line[8] = line[8][line[8].find("gene:ENSDAR")+5:line[8].find("gene:ENSDAR")+23]

            f.write("INSERT INTO `Transcripts104`(`Chromosome`, `Annotation_Provider`, `Type`, `Start_Position`, `End_Position`, `Dots`, `Dash`, `Number`, `Transcript_ID`) VALUES ({0},'{1}','{2}',{3},{4},'{5}','{6}','{7}','{8}');".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))


# FOR THE GeneCategories TABLE

f.write("CREATE TABLE `GeneCategories` (`ReleaseNo` int(11) DEFAULT NULL,`mRNA` int(11) DEFAULT NULL,`three_prime_UTR` int(11) DEFAULT NULL,`exon` int(11) DEFAULT NULL,`CDS` int(11) DEFAULT NULL,`five_prime_UTR` int(11) DEFAULT NULL,`biological_region` int(11) DEFAULT NULL,`ncRNA_gene` int(11) DEFAULT NULL,`lnc_RNA` int(11) DEFAULT NULL,`rRNA` int(11) DEFAULT NULL,`snoRNA` int(11) DEFAULT NULL,`pseudogene` int(11) DEFAULT NULL,`pseudogenic_transcript` int(11) DEFAULT NULL,`miRNA` int(11) DEFAULT NULL);")

f.write("INSERT INTO `GeneCategories` (`ReleaseNo`, `mRNA`, `three_prime_UTR`, `exon`, `CDS`, `five_prime_UTR`, `biological_region`, `ncRNA_gene`, `lnc_RNA`, `rRNA`, `snoRNA`, `pseudogene`, `pseudogenic_transcript`, `miRNA`) VALUES(104, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12});".format(dict['mRNA'], dict['three_prime_UTR'], dict['exon'], dict['CDS'], dict['five_prime_UTR'], dict['biological_region'], dict['ncRNA_gene'], dict['lnc_RNA'], dict['rRNA'], dict['snoRNA'], dict['pseudogene'], dict['pseudogenic_transcript'], dict['miRNA']))


# FOR THE ReleaseInfo TABLE

f.write("CREATE TABLE `ReleaseInfo` (`ReleaseNo` int(11) NOT NULL,`Chromosome` int(11) NOT NULL,`UniqueTranscripts` int(11) DEFAULT NULL);")

f.write("INSERT INTO `ReleaseInfo` (`ReleaseNo`, `Chromosome`, `UniqueTranscripts`) VALUES(104, 12, {0});".format(len(transcript_set)))


# FOR THE TRANSCRIPTS100 TABLE

FH = open("Danio_rerio.GRCz11.100.chromosome.12.gff3", 'r')

transcript_set = set()
dict2 = {}

f.write("CREATE TABLE `Transcripts100` (`Chromosome` int(60) DEFAULT NULL,`Annotation_Provider` varchar(60) DEFAULT NULL,`Type` varchar(60) DEFAULT NULL,`Start_Position` int(60) DEFAULT NULL,`End_Position` int(60) DEFAULT NULL,`Dots` varchar(60) DEFAULT NULL,`Dash` varchar(60) DEFAULT NULL,`Number` varchar(60) DEFAULT NULL,`Transcript_ID` varchar(1000) DEFAULT NULL);")

for i in FH:
    if not i.startswith('#'):
        line = i.strip().split('\t')
        if line[2] not in dict2.keys():
            dict2[str(line[2])] = 1
        else:
            dict2[str(line[2])] += 1

        if len(line) == 9:
            if "transcript:ENSDART" in line[8]:
                line[8] = line[8][line[8].find("transcript:ENSDART")+11:line[8].find("transcript:ENSDART")+29]
                transcript_set.add(line[8])
            if "gene:ENSDAR" in line[8]:
                line[8] = line[8][line[8].find("gene:ENSDAR")+5:line[8].find("gene:ENSDAR")+23]

            f.write("INSERT INTO `Transcripts100`(`Chromosome`, `Annotation_Provider`, `Type`, `Start_Position`, `End_Position`, `Dots`, `Dash`, `Number`, `Transcript_ID`) VALUES ({0},'{1}','{2}',{3},{4},'{5}','{6}','{7}','{8}');".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))


# FOR THE GeneCategories TABLE

f.write("INSERT INTO `GeneCategories` (`ReleaseNo`, `mRNA`, `three_prime_UTR`, `exon`, `CDS`, `five_prime_UTR`, `biological_region`, `ncRNA_gene`, `lnc_RNA`, `rRNA`, `snoRNA`, `pseudogene`, `pseudogenic_transcript`, `miRNA`) VALUES(100, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12});".format(dict2['mRNA'], dict2['three_prime_UTR'], dict2['exon'], dict2['CDS'], dict2['five_prime_UTR'], dict2['biological_region'], dict2['ncRNA_gene'], dict2['lnc_RNA'], dict2['rRNA'], dict2['snoRNA'], dict2['pseudogene'], dict2['pseudogenic_transcript'], dict2['miRNA']))

# FOR THE ReleaseInfo TABLE

f.write("INSERT INTO `ReleaseInfo` (`ReleaseNo`, `Chromosome`, `UniqueTranscripts`) VALUES(100, 12, {0});".format(len(transcript_set)))


f.close()

