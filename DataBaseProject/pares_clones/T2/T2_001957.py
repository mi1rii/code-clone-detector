def is_sorted(lst) :
	it = iter(lst)
	try :
		prev = it.next()
	except StopIteration :
		return True
	for x in it :
		if prev > x :
			return False
		prev = x
	return True


def var_1(var_2) :
	var_3 = var_4(var_2)
	try :
		var_5 = var_3.var_6()
	except var_7 :
		return True
	for var_8 in var_3 :
		if var_5 > var_8 :
			return False
		var_5 = var_8
	return True
