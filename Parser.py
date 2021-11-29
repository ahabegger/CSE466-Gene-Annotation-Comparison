

FH = open("Danio_rerio.GRCz11.100.chromosome.12.gff3", 'r')

dict = dict()

for i in FH:
    if not i.startswith('#'):
        line = i.strip().split('\t')
        if line[2] not in dict.keys():
            dict[str(line[2])] = 1
        else:
            dict[str(line[2])] += 1

for key in dict.keys():
    print("{0} : {1}".format(key, dict[key]))


# First is chromosome
