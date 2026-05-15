def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
			while next(seq) ! = x : pass
		else :
			return True
	except StopIteration :
		pass
	return False


def var_1(var_2, var_3) :
	var_4 = var_5(var_3)
	try :
		for var_6 in var_2 :
			while var_7(var_4) ! = var_6 : pass
		else :
			return True
	except var_8 :
		pass
	return False
