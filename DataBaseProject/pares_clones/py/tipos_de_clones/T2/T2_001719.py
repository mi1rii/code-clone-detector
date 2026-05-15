def consec(n, iterable) :
	result = set()
	prev = None
	count = 0
	for item in iterable :
		if item == prev :
			count += 1
			if count == n :
				result.add(prev)
		else :
			prev = item
			count = 1
	return result


def var_1(var_2, var_3) :
	var_4 = set()
	var_5 = None
	var_6 = 0
	for var_7 in var_3 :
		if var_7 == var_5 :
			var_6 += 1
			if var_6 == var_2 :
				var_4.var_8(var_5)
		else :
			var_5 = var_7
			var_6 = 1
	return var_4
