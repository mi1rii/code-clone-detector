def func(t, freq, offset, * args) :
	an = []
	bn = []
	for i in range(len(args)) :
		if i % 2 == 0 :
			an.append(args [i])
		else :
			bn.append(args [i])
	result = 0
	pairs = zip(an, bn)
	for (q, ab) in zip(params, pairs) :
		ai, bi = ab
		result += ai * np.sin(q * freq * t) + bi * np.cos(q * freq * t)
	return result


def var_1(var_2, var_3, var_4, * var_5) :
	var_6 = []
	var_7 = []
	for var_8 in range(len(var_5)) :
		if var_8 % 2 == 0 :
			var_6.var_9(var_5 [var_8])
		else :
			var_7.var_9(var_5 [var_8])
	var_10 = 0
	var_11 = zip(var_6, var_7)
	for (var_12, var_13) in zip(var_14, var_11) :
		var_15, var_16 = var_13
		var_10 += var_15 * var_17.var_18(var_12 * var_3 * var_2) + var_16 * var_17.var_19(var_12 * var_3 * var_2)
	return var_10
