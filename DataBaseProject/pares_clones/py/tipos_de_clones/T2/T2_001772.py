def flatten(seq) :
	l = []
	for elt in seq :
		t = type(elt)
		if t is tuple or t is list :
			for elt2 in flatten(elt) :
				l.append(elt2)
		else :
			l.append(elt)
	return l


def var_1(var_2) :
	var_3 = []
	for var_4 in var_2 :
		var_5 = var_6(var_4)
		if var_5 is tuple or var_5 is list :
			for var_7 in var_1(var_4) :
				var_3.var_8(var_7)
		else :
			var_3.var_8(var_4)
	return var_3
