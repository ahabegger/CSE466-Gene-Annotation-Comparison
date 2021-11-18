import pprint
from BCBio.GFF import GFFExaminer
from BCBio import GFF


in_file = "Danio_rerio.GRCz11.104.chromosome.12.validated.gff3"
examiner = GFFExaminer()

# with open(in_file) as f:
#     pprint.pprint(examiner.parent_child_map(f))
#
with open(in_file) as f:
    pprint.pprint(examiner.available_limits(f))

limit_info = dict(gff_type=["mRNA"])

with open("Danio_rerio.GRCz11.104.chromosome.12.validated.gff3") as f:
    for rec in GFF.parse(f, limit_info=limit_info,  target_lines=20):
        # print(rec.__dict__.keys())
        # print(rec.features)
        # print(len(rec.features))
        for feature in rec.features:
            print(feature.location, feature.id, feature.qualifiers['ID'], feature.qualifiers['geneID'])