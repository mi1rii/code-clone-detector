def is_sorted(lst) :
	try :
		sorted(lst, cmp = my_cmp)
		return True
	except ValueError :
		return False


def var_1(var_2) :
	try :
		sorted(var_2, var_3 = var_4)
		return True
	except var_5 :
		return False
