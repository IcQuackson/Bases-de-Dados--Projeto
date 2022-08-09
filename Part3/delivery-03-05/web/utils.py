




def make_friendly(error):
	try:
		message = error.diag.message_primary
		e_code = error.pgcode
		hint = error.diag.message_hint
		codeClass = int(error.pgcode[:-3])
	except:
		message = str(error)
		codeClass = -1
		e_code = -1
		hint = ''

	isBadData = codeClass == 22 
	isIntegrityConstrain = 23 == codeClass
	isUniqueConstrain = e_code == '23505'

	# hints are created in triggers and only provide user level information 
	if hint:
		return hint
	
	usefullToUser = isBadData or isIntegrityConstrain
	if usefullToUser is True:
			# There are statistics that say that the closer a deadline is the worst are the solutions...
			if 'duplicate key value violates unique constraint "product_pkey"' == message:
				return "Product already exists."
			if 'insert or update on table "supplies_sec" violates foreign key constraint "supplies_sec_nif_fkey"' == message:
				return "Secondary supplier does not exist."
			if 'insert or update on table "supplies_prim" violates foreign key constraint "supplies_prim_nif_fkey"' == message:
				return "Primary supplier does not exist."
			if 'duplicate key value violates unique constraint "supplies_sec_pkey"' == message:
				return "Secondary supplier already added."
			if 'duplicate key value violates unique constraint "supplies_prim_nif_pkey"' == message:
				return "Primary supplier already added."
			if 'insert or update on table "product" violates foreign key constraint "product_associated_to_name_fkey"' == message:
				return "Invalid category"
			if 'update or delete on table "supplier" violates foreign key constraint "supplies_prim_nif_fkey" on table "supplies_prim"' == message:
				return "Cannot delete supplier because there are products that depend on him."
			if 'update or delete on table "supplier" violates foreign key constraint "supplies_sec_nif_fkey" on table "supplies_sec"' ==message:
				return "Cannot perform operation on supplier because there are products that depend on him."


			# inserted after seeing raw message in pergunta_a
			if 'update or delete on table "category" violates foreign key constraint "product_associated_to_name_fkey" on table "product"' == message:
				return 'Cannot perform operation on category. It has dependencies!'
		



			# generic error messages
		
			if isBadData:
				return "Bad form data. Please verify the form fields."		
			if isUniqueConstrain:
				return "Tried to create or add an already created/added object."  
	else:
		return message
		return 'Internal Error'
	
