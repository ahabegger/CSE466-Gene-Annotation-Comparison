#!/usr/bin/env python3

import cgi,cgitb,pymysql
cgitb.enable()
# Create instance/object of Field Storage
form=cgi.FieldStorage()
db = pymysql.connect(host="localhost",  # your host 
                     user="habeggaj",       # username
                     passwd="bio466",     # password
                     db="habeggaj")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM `ReleaseInfo` WHERE ReleaseNo = 100;")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Release Compare</title>")
print("</head>")
print("<body>")
print("<h1> CSE 466 Final Project</h1>")
print("<h3> Alex Habegger and Lily Hofman</h3>")

print("<h2>Release 100 - Chromosome 12</h2>")

print("<p>Release Information</p>") 
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>Release Number</th><th>Chromosome Number</th><th>Categories of Genes</th><th>Unique Transcript Number</th></tr>")   
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2]) + "</td><td>"  + str(row[3]) + "</td></tr>")
print ("</table>")

cur.execute("SELECT * FROM `GeneCategories` WHERE ReleaseNo = 100;")

print("<p>Gene Category Information</p>") 
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>mRNA</th><th>three_prime_UTR</th><th>exon</th><th>CDS</th><th>five_prime_UTR</th><th>biological_region</th><th>ncRNA_gene</th><th>lnc_RNA</th><th>rRNA</th><th>snoRNA</th><th>pseudogene</th><th>pseudogenic_transcript</th><th>miRNA</th></tr>")   
for row in cur.fetchall() :
    print("<tr>", end="")
    for x in range(1, len(row)):
        print("<td>", end="")
        print(str(row[x]))
        print("</td>")
    print("<tr>", end="")
print ("</table>")


print("<h2>Release 104 - Chromosome 12</h2>")
cur.execute("SELECT * FROM `ReleaseInfo` WHERE ReleaseNo = 104;")

print("<p>Release Information</p>") 
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>Release Number</th><th>Chromosome Number</th><th>Categories of Genes</th><th>Unique Transcript Number</th></tr>")   
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2]) + "</td><td>"  + str(row[3]) + "</td></tr>")
print ("</table>")

cur.execute("SELECT * FROM `GeneCategories` WHERE ReleaseNo = 104;")

print("<p>Gene Category Information</p>") 
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>mRNA</th><th>three_prime_UTR</th><th>exon</th><th>CDS</th><th>five_prime_UTR</th><th>biological_region</th><th>ncRNA_gene</th><th>lnc_RNA</th><th>rRNA</th><th>snoRNA</th><th>pseudogene</th><th>pseudogenic_transcript</th><th>miRNA</th></tr>")   
for row in cur.fetchall() :
    print("<tr>", end="")
    for x in range(1, len(row)):
        print("<td>", end="")
        print(str(row[x]))
        print("</td>")
    print("<tr>", end="")
print ("</table>")

print("<a href=\"./index.html\" class=\"btn btn-success center\" role=\"button\" aria-pressed=\"true\">Back</a>")

print("<style>")
print(".center {")
print(" text-align: center;")
print("}")
print("</style>")

cur.close()
del cur
db.close()

print("</body>")
print("</html>")
