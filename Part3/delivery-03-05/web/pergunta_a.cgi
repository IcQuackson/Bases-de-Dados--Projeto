#!/usr/bin/python3
try:
	import sys
	sys.stderr = sys.stdout
	import cgi
	import cgitb
	cgitb.enable()
	import urllib.parse as urlparse
	from randfacts import getFact

	import htmlstuff
	import json
	from utils import make_friendly
	import scriptsstuff

	import os
	import psycopg2
	from login import *
	

except Exception as e:
	print(htmlstuff.webpagehead)
	print(e)
	exit(0)




# coisas a descobrir:
# obter methodo do resquest
# obter cada variavel
def cgiFieldStorageToDict(fieldStorage):
   """ Get a plain dictionary rather than the '.value' system used by the 
   cgi module's native fieldStorage class. """
   params = {}
   for key in fieldStorage.keys(  ):
      params[key] = fieldStorage[key].value
   return params

# field storage only works on get method for some reason
# any kind of binary data cannot be sent in the get method
try:
	fStorage = cgi.FieldStorage()
except Exception as e:
	print(e)
	exit(0)



# GLOBAL VARS
data = cgiFieldStorageToDict(fStorage)



# performs action an returns original page
def handle_logic(cursor):
		tp = data['type']
		if tp == "Simple Category":
			table = "simple_category"
		elif tp == "Super Category":
			table = "super_category"
		else:
			raise Exception(f"Invalid value type of category: {tp}.")
	


		op = data['operation'].upper()
		if op == 'INSERT':
			baseQuery = ["INSERT INTO category VALUES (%s)",\
"INSERT INTO $ VALUES (%s)".replace('$',table)]
		elif op == 'DELETE':
			baseQuery = ["DELETE FROM $ c WHERE c.name = %s".replace('$',table),\
"DELETE FROM category c WHERE c.name =  %s" ]
		else:
			raise Exception(f"Invalid value of operation {op}.")	
	
		cursor = connection.cursor()
		result = cursor.execute(baseQuery[0], (data['category'],) )	
		result = cursor.execute(baseQuery[1], (data['category'],) )	
		connection.commit()

		
	


def handle_webpage_request(cursor):
	print(htmlstuff.manage_categories_form)


	# Get all categories of all types
	sql = 'SELECT * FROM simple_category;'; cursor.execute(sql)
	simple_categories = (cursor.fetchall(),  "Simple Category")
	sql = 'SELECT * FROM super_category;'; cursor.execute(sql)
	super_categories = (cursor.fetchall(), "Super Category")
	# Display results
	print('<p>There are ', len(simple_categories[0]), 'simple categories and \
	',len(super_categories[0]), ' super categories.</p>')
	type_of_row = simple_categories[1]
	for row in simple_categories[0]:
		dtfields = {'name':row[0], 'type':type_of_row}
		print(htmlstuff.category_row.format(**dtfields))

	type_of_row = super_categories[1]
	for row in super_categories[0]:
		dtfields = {'name':row[0], 'type':type_of_row}
		print(htmlstuff.category_row.format(**dtfields))

	# add scripts of interactivity
 	# cgi detects if an request is a form submit if it has url params, this allows us to go back to return to the original state when performing an action 
	print(scriptsstuff.preserveURL.format("pergunta_a"))


	cursor.close()





def main(connection): 
	try:
		print(htmlstuff.webpagehead)

		cursor = connection.cursor()

		if data.get('type', None) or data.get('operation', None):
				handle_logic(cursor)	
				print(htmlstuff.success.format("Operation Successful!", getFact())) 

	except psycopg2.IntegrityError as e:   
		connection.rollback()
		err = make_friendly(e)
		print( htmlstuff.error.format(err) )
	except Exception as e:    
		# print exception
		connection.rollback()  # if the transaction is successful it will have no effect, but it feels wrong to be inside finally
		if str(e) == "Unexpected form data!":
			err = str(e)
		else:
			err = make_friendly(e)
		print( htmlstuff.error.format(err) )
	finally:
		handle_webpage_request(cursor)
		cursor.close()
		print("</body></html>")
			



connection = psycopg2.connect(credentials)
main(connection)
if connection:
	connection.close()




