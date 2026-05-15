def sublist(a, b) :
	last = 0
	for el_a in a :
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
			return False
	return True


def var_1(var_2, var_3) :
	var_4 = 0
	for var_5 in var_2 :
		if var_5 in var_3 [var_4 :] :
			var_4 = var_3 [var_4 :].var_6(var_5)
		else :
			return False
	return True
