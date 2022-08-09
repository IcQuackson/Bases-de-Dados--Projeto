#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>List sub categories</title>')

print('<style>')
print('table {')
print('font-family: arial, sans-serif;')
print('border-collapse: collapse;')
print('width: 50%;}')

print('td {')
print('border: 1px solid #dddddd;')
print('text-align: left;')
print('padding: 8px;}')

print('tr:nth-child(even) {')
print('background-color: #dddddd;}')
print('</style>')

print('</head>')
print('<body>')
print('<h3>Super Categories</h3>')
connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT name FROM super_category;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Displaying results
    print('<table border="0" cellspacing="5">')
    print('<tr><td style="font-weight: bold;">super category</td><td></td> </tr>')
    for row in result:
        print('<tr>')
        for value in row:
        # The string has the {}, the variables inside format() will replace the{}
            print('<td>{}</td>'.format(value))

        sql = 'SELECT category_name FROM consists_of WHERE super_category_name = %(category_name)s;'
        cursor = connection.cursor()
        cursor.execute(sql, {'category_name': row[0]})
        sub_result = cursor.fetchall()
        count = len(sub_result)
        if count > 0:
            print('<td><a href="list_sub_aux.cgi?name={}">See sub-categories</a></td>'.format(row[0]))
        else:
            print('<td style="color: #7d827e;">No sub categories</td>') 
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

