def merge_dicts(d1, d2) :
	try :
		intersection = d1.viewkeys() & d2
	except AttributeError :
		intersection = d1.keys() & d2
	if any(d1 [shared] ! = d2 [shared] for shared in intersection) :
		return {}
	return dict(d1, ** d2)


def var_1(var_2, var_3) :
	try :
		var_4 = var_2.var_5() & var_3
	except var_6 :
		var_4 = var_2.var_7() & var_3
	if any(var_2 [var_8] ! = var_3 [var_8] for var_8 in var_4) :
		return {}
	return dict(var_2, ** var_3)
