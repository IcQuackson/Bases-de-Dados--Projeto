#!/usr/bin/python3
import psycopg2
import login
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Replenishments</title>')

print('<style>')
print('table {')
print('font-family: arial, sans-serif;')
print('border-collapse: collapse;')
print('width: 100%;}')

print('th {')
print('border: 1px solid #dddddd;')
print('text-align: left;')
print('background-color: #4CAF50;')
print('color: white;')
print('padding: 8px;}')

print('td {')
print('border: 1px solid #dddddd;')
print('text-align: left;')
print('padding: 8px;}')

print('tr:nth-child(even) {')
print('background-color: #dddddd;}')
print('</style>')

print('</head>')
print('<body>')
print('<h3 style="color:#4CAF50;">Products</h3>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT ean, descr, associated_to_name FROM product;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)
    
    # Displaying results
    print('<table border="0" cellspacing="5">')

    print('<tr>')
    print('<th>ean</th>')
    print('<th>description</th>')
    print('<th>category</th>')
    print('<th></th>')

    for row in result:
        print('<tr>')
        for value in row:
    # The string has the {}, the variables inside format() will replace the {}
            print('<td>{}</td>'.format(value))
        print('<td><a href="ShowReplenishments.cgi?ean={}">Replenishments</a></td>'.format(row[0]))
        print('</tr>')
    print('</table>')

    # Closing connection
    cursor.close()

except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()
print('</body>')
print('</html>')

