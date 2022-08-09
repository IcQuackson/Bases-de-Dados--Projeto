#!/usr/bin/python3


# SEE the end of the file for the entry point
try:
	import sys
	sys.stderr = sys.stdout
	# make my imports available to apache
	import cgi
	import cgitb
	cgitb.enable()
	import urllib.parse as urlparse

	import htmlstuff
	import scriptsstuff
	from utils import make_friendly

	from collections import defaultdict
	from string import Formatter
	import time
	from datetime import date


	import json
	from randfacts import getFact
	import os
	import psycopg2
	from login import *
	

except Exception as e:
	print(htmlstuff.webpagehead)
	print(e)
	exit(0)


dev_mode = True


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
data = cgiFieldStorageToDict(fStorage)



def add_suppliers_to_product(cursor):
	secs = []
	prim = data.get('supplierprim', None)
	secs.append(data.get('suppliersec1', None))
	secs.append(data.get('suppliersec2', None))
	secs.append(data.get('suppliersec3', None))
	if not data.get('ean', None) or not (prim or secs):
		raise Exception("Unexpected form data!")

	if prim:
		query = "INSERT INTO supplies_prim (nif, ean, since) VALUES(%s,%s,%s)"
		params = (prim, data['ean'], date.today() )
		cursor.execute(query, params ) 
	for sup in secs:
		if sup:
				query = "INSERT INTO supplies_sec (nif, ean) VALUES(%s,%s)"
				params = (sup, data['ean'])
				cursor.execute(query, params ) 
	connection.commit()

def remove_product(cursor):
	clean_up_queries = [ "DELETE FROM replenish_event WHERE product_ean = %s", "DELETE FROM planogram WHERE product_ean = %s ",
					 	"DELETE FROM supplies_prim WHERE ean = %s", 
						"DELETE FROM supplies_sec WHERE ean = %s", "DELETE FROM product WHERE ean = %s"]
	for q in clean_up_queries:
		cursor.execute(q, (data['ean'],))
			
	connection.commit()
	
def add_product(cursor):
		try:
			if not ( data['supplierprim'] and data['ean'] and data['description'] and data['category']):
				raise Exception("Unexpected form data!")
		except:
			raise Exception("Unexpected form data!")

		query = "INSERT INTO product (ean, descr, associated_to_name) VALUES(%s,%s,%s)"
		cursor.execute(query, (data['ean'], data['description'], data['category']))
		query = "INSERT INTO supplies_prim (nif,ean,since) VALUES (%s,%s,%s)"
		cursor.execute(query, (data['supplierprim']	, data['ean'], date.today(),)  )
		
		connection.commit()

def remove_supplier_from_product(cursor):
	query =  "DELETE FROM supplies_prim WHERE nif = %s and ean = %s"	
	cursor.execute(query, (data['mp_nif'], data['mp_ean']))	
	query =  "DELETE FROM supplies_sec WHERE nif = %s and ean = %s"
	cursor.execute(query, (data['mp_nif'], data['mp_ean']))	
	connection.commit()


def create_supplier(cursor):
	query = "INSERT INTO supplier (nif,name) VALUES(%s,%s)"
	cursor.execute(query, (data['ms_nif'],data['ms_name']))
	connection.commit()

def delete_supplier(cursor):
	cleanup_queries = [	"DELETE FROM supplier WHERE nif = %s" ]
	for q in cleanup_queries:
		cursor.execute(q, (data['ms_nif'],))

	connection.commit()




def main(connection): 
	try:

		print(htmlstuff.webpagehead)

		cursor = connection.cursor()

		operation_text = None
		operation = data.get('operation', None)
		# update 'objects'
		if operation == 'updateSuppliers':
			add_suppliers_to_product(cursor)
			operation_text = "Supplier added to product"
		elif operation == 'deleteSuppliers':
			remove_supplier_from_product(cursor)

		# create or delete 'objects'
		elif operation == 'createProduct':
			add_product(cursor)
			# use of cool facts because the state of the page must change between successfull operations
			operation_text = "Product created successfully"
		elif operation == 'DELETE':
			remove_product(cursor)	
			operation_text = "Product deleted successfully"


		elif operation == 'CREATESUPPLIER': 
			print(scriptsstuff.scrollToSuppliers) 
			create_supplier(cursor)	
			operation_text = "Supplier created successfully"
		elif operation == 'DELETESUPPLIER':
			print(scriptsstuff.scrollToSuppliers) 
			delete_supplier(cursor)	
			operation_text = "Supplier deleted successfully"
	

		if operation_text:
				print(htmlstuff.success.format(operation_text, getFact())) 

	except psycopg2.IntegrityError as e:   
		connection.rollback()  # if the transaction is successful it will have no effect, but it feels wrong to be inside finally
		err = make_friendly(e)
		print( htmlstuff.error.format(err) )
	except Exception as e:    
		connection.rollback()
		# print exception
		if str(e) == "Unexpected form data!":
			err = str(e)
		else:
			err = make_friendly(e)
		print( htmlstuff.error.format(err) )
	finally:
		handle_webpage_request(cursor)
		cursor.close()
			


def form_memory(form):
	# get all the names of the python format variables in the form template
	form_fields = [fn for _, fn, _, _ in Formatter().parse(form) if fn is not None]
	fmemory = {}	
	# generate all the form fields either from url params or from the default value ''	
	for field in form_fields:
		fmemory[field] = data.get(field, '')
	return form.format(**fmemory) # ** to expand dict to key=value pairs


def handle_webpage_request(cursor):
	# restore url since we are not using post requests
	print(scriptsstuff.preserveURL.format("pergunta_b"))

	product_form = form_memory(htmlstuff.create_product_form)
	supplier_form = form_memory(htmlstuff.create_delete_supplier_form)
	sup_form = form_memory(htmlstuff.modify_product_suppliers_form)

	print("<div><div style='display:inline-block;")
	print(product_form)
	print("</div>")

	print("<div style='display:inline-block;'>")
	print(supplier_form)
	print("</div>")

	print("<div style='display:inline-block;'>")
	print(sup_form)
	print("</div>")

	print("</div>")


	print('<p>Note: There is a list of all suppliers on the bottom of the page</p>')
	
	sql = 'SELECT * FROM supplier;'; cursor.execute(sql)
	suppliers = cursor.fetchall()

	# Show products
	sql = 'SELECT * FROM product P NATURAL JOIN supplies_prim SP ORDER BY SP.since'; cursor.execute(sql)
	products = cursor.fetchall()
	print('<p>Currently there are ', len(products), " products.")
	for p in products:
		row_data = { 'ean':p[0], 'description':p[1], 'category':p[2], 'primary' : p[3]  }
		print(htmlstuff.product_row.format(**row_data))
	
	
	# show suppliers to assist creation of products
	print(f'<div id="supplierstable"><h3>Suppliers</h3> ') 
	print('<p>Currently there are ', len(suppliers), " suppliers.")

	for sup in suppliers:
		props = {'name' : sup[1], 'nif':sup[0], 'style': htmlstuff.remove_style}
		print(f'<div style="{htmlstuff.row_css}">') 	
		print(htmlstuff.supplier_row.format(**props)) 
		print('</div>')

	print("</div")
	
	
	
	

# ENTRY POINT

connection = psycopg2.connect(credentials)
main(connection)
if connection:
	connection.close()





