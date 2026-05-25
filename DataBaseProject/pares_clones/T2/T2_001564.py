def unique(items) :
	seen = set()
	for i in xrange(len(items) - 1, - 1, - 1) :
		it = items [i]
		if it in seen :
			del items [i]
		else :
			seen.add(it)


def var_1(var_2) :
	var_3 = set()
	for var_4 in var_5(len(var_2) - 1, - 1, - 1) :
		var_6 = var_2 [var_4]
		if var_6 in var_3 :
			del var_2 [var_4]
		else :
			var_3.var_7(var_6)
