#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()

ean = form.getvalue('ean')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Change Designation</title>')
print('</head>')
print('<body>')

# The string has the {}, the variables inside format() will replace the {}
print('<h3 style = "color:#3256a8;" >Change designation for product {}</h3>'.format(ean))

# The form will send the info needed for the SQL query
print('<form action="update_designation.cgi" method="post">')
print('<p><input type="hidden" name="ean" value="{}"/></p>'.format(ean))
print('<p>New designation: <input type="text" name="designation" required/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>')
print('</html>')

