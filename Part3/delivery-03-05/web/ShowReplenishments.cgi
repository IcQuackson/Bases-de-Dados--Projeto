#!/usr/bin/python3
import psycopg2, cgi
import login


form = cgi.FieldStorage()
#getvalue uses the names from the form in previous page
ean = form.getvalue('ean')

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

connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT * FROM replenish_event where product_ean = %(ean)s;'
    data = ean
    
    # The string has the {}, the variables inside format() will replace the {}
    print('<p>{}</p>'.format(sql % ({'ean': ean})))
    # Feed the data to the SQL query as follows to avoid SQL injection
    cursor.execute(sql, {'ean': ean})
    result = cursor.fetchall()
    num = len(result)

    print('<table border="0" cellspacing="5">')
    print('<tr>')
    print('<th>Product_ean</th>')
    print('<th>supermarket_NIF</th>')
    print('<th>corridor_nr</th>')
    print('<th>shelf_side</th>')
    print('<th>shelf_height</th>')
    print('<th>instant</th>')
    print('<th>units</th>')
    print('<tr>')
    for row in result:
        print('<tr>')
        for value in row:
    # The string has the {}, the variables inside format() will replace the {}
            print('<td>{}</td>'.format(value))
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

