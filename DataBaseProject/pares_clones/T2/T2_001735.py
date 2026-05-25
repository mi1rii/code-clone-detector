def a(name) :
	global_variables = globals()
	try :
		name_of_passed_in_variable = [x for x in global_variables if id(global_variables [x]) == id(name)] [0]
	except Exception :
		name_of_passed_in_variable = "unknown"
	print name_of_passed_in_variable, name


def var_1(var_2) :
	var_3 = var_4()
	try :
		var_5 = [var_6 for var_6 in var_3 if var_7(var_3 [var_6]) == var_7(var_2)] [0]
	except var_8 :
		var_5 = "unknown"
	print var_5, var_2
