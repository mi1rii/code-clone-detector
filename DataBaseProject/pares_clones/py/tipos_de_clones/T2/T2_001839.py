def sublist(a, b) :
	i = - 1
	try :
		for e in a :
			i = b.index(e, i + 1)
	except ValueError :
		return False
	else :
		return True


def var_1(var_2, var_3) :
	var_4 = - 1
	try :
		for var_5 in var_2 :
			var_4 = var_3.var_6(var_5, var_4 + 1)
	except var_7 :
		return False
	else :
		return True
