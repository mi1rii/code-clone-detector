def future6(A) :
	known = []
	result = []
	for idx in xrange(len(A) - 1, - 1, - 1) :
		value = A [idx]
		known = [(x, y) for x, y in known if y > value]
		if known :
			result.append(known [- 1] [0])
		else :
			result.append(- 1)
		known.append((idx, value))
	return np.array(result) [: : - 1]


def var_1(var_2) :
	var_3 = []
	var_4 = []
	for var_5 in var_6(len(var_2) - 1, - 1, - 1) :
		var_7 = var_2 [var_5]
		var_3 = [(var_8, var_9) for var_8, var_9 in var_3 if var_9 > var_7]
		if var_3 :
			var_4.var_10(var_3 [- 1] [0])
		else :
			var_4.var_10(- 1)
		var_3.var_10((var_5, var_7))
	return var_11.var_12(var_4) [: : - 1]
