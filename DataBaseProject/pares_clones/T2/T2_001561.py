def wrapper(arg1) :
	result = func(arg1)
	for err in findError(result) :
		errors.append(err)
	print errors
	return result


def var_1(var_2) :
	var_3 = var_4(var_2)
	for var_5 in var_6(var_3) :
		var_7.var_8(var_5)
	print var_7
	return var_3
