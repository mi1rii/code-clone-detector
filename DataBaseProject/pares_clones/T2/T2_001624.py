def convertType(value) :
	try :
		return int(value) if value.strip().isdigit() else float(value)
	except :
		return value


def var_1(var_2) :
	try :
		return int(var_2) if var_2.var_3().var_4() else float(var_2)
	except :
		return var_2
