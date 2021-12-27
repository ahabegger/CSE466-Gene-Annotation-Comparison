#!/usr/bin/env python3
#####This causes problem #!/usr/bin/python3.7
import cgi,cgitb,pymysql
cgitb.enable()
# Create instance/object of Field Storage
form=cgi.FieldStorage()
GeneID=form.getvalue('GeneID')

db = pymysql.connect(host="localhost",  # your host 
                     user="habeggaj",       # username
                     passwd="bio466",     # password
                     db="habeggaj")   # name of the database

cur = db.cursor()


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Gene Compare</title>")
print("</head>")
print("<body>")
print("<h2>Gene ID : {0}</h2>".format(GeneID))

print("<h3>Release 100</h2>")
cur.execute("SELECT * FROM `Transcripts100` WHERE Transcript_ID = '{0}';".format(GeneID))
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>Chromosome</th><th>Annotation Provider</th><th>Type</th><th>Start Position</th><th>End Position</th><th>Score</th><th>Strand</th><th>Phase</th><th>ID</th></tr>")   
for row in cur.fetchall() :
    print("<tr>", end="")
    for x in range(0, len(row)):
        print("<td>", end="")
        print(str(row[x]))
        print("</td>")
    print("<tr>", end="")
print ("</table>")

cur.execute("SELECT * FROM `Transcripts100` WHERE Transcript_ID = '{0}';".format(GeneID))

start_pos = 0
end_pos = 0
for row in cur.fetchall():
    start_pos = row[3]
    end_pos = row[4]
    print("<p>Gene Length : {0}</p>".format(row[4]-row[3]))

cur.execute("SELECT COUNT(*) FROM `Transcripts100` WHERE Type = 'exon' and Start_Position >= {0} and End_Position <= {1};".format(start_pos, end_pos))

for row in cur.fetchall():
    print("<p>Exon Number: {0}</p>".format(row[0]))

print("<h3>Release 104</h2>")
cur.execute("SELECT * FROM `Transcripts104` WHERE Transcript_ID = '{0}';".format(GeneID))
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>Chromosome</th><th>Annotation Provider</th><th>Type</th><th>Start Position</th><th>End Position</th><th>Score</th><th>Strand</th><th>Phase</th><th>ID</th></tr>")   
for row in cur.fetchall() :
    print("<tr>", end="")
    for x in range(0, len(row)):
        print("<td>", end="")
        print(str(row[x]))
        print("</td>")
    print("<tr>", end="")
print ("</table>")

cur.execute("SELECT * FROM `Transcripts104` WHERE Transcript_ID = '{0}';".format(GeneID))

start_pos = 0
end_pos = 0
for row in cur.fetchall():
    start_pos = row[3]
    end_pos = row[4]
    print("<p>Gene Length : {0}</p>".format(row[4]-row[3]))

cur.execute("SELECT COUNT(*) FROM `Transcripts104` WHERE Type = 'exon' and Start_Position >= {0} and End_Position <= {1};".format(start_pos, end_pos))

for row in cur.fetchall():
    print("<p>Exon Number: {0}</p>".format(row[0]))

cur.close()
del cur
db.close()


print("</body>")
print("</html>")
