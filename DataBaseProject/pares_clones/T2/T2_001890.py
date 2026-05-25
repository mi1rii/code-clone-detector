def merge(x) :
	if len(x) == 1 :
		return x
	else :
		mid = int(len(x) / 2)
		l = merge(x [: mid])
		r = merge(x [mid :])
	i = j = 0
	result = []
	while i < len(l) and j < len(r) :
		if l [i] < r [j] :
			result.append(l [i])
			i += 1
		else :
			result.append(r [j])
			j += 1
	result += l [i :]
	result += r [j :]
	return result


def var_1(var_2) :
	if len(var_2) == 1 :
		return var_2
	else :
		var_3 = int(len(var_2) / 2)
		var_4 = var_1(var_2 [: var_3])
		var_5 = var_1(var_2 [var_3 :])
	var_6 = var_7 = 0
	var_8 = []
	while var_6 < len(var_4) and var_7 < len(var_5) :
		if var_4 [var_6] < var_5 [var_7] :
			var_8.var_9(var_4 [var_6])
			var_6 += 1
		else :
			var_8.var_9(var_5 [var_7])
			var_7 += 1
	var_8 += var_4 [var_6 :]
	var_8 += var_5 [var_7 :]
	return var_8
