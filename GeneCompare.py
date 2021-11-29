#!/usr/bin/env python3
#####This causes problem #!/usr/bin/python3.7
import cgi,cgitb
cgitb.enable()
# Create instance/object of Field Storage
form=cgi.FieldStorage()
first_name=form.getvalue('FirstName')
last_name=form.getvalue('LastName')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")