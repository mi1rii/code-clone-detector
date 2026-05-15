def to_bool(bool_str) :
	if isinstance(bool_str, basestring) and bool_str :
		if bool_str.lower() in ['true', 't', '1'] : return True
		elif bool_str.lower() in ['false', 'f', '0'] : return False
	raise ValueError("%s is no recognized as a boolean value" % bool_str)


def var_1(var_2) :
	if isinstance(var_2, var_3) and var_2 :
		if var_2.var_4() in ['true', 't', '1'] : return True
		elif var_2.var_4() in ['false', 'f', '0'] : return False
	raise var_5("%s is no recognized as a boolean value" % var_2)
