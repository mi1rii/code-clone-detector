def merge(left, right) :
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right) :
		if left [i] < right [j] :
			result.append(left [i])
			i += 1
		else :
			result.append(right [j])
			j += 1
	result.extend(left [i :])
	result.extend(right [j :])
	return result


def var_1(var_2, var_3) :
	var_4 = []
	var_5, var_6 = 0, 0
	while var_5 < len(var_2) and var_6 < len(var_3) :
		if var_2 [var_5] < var_3 [var_6] :
			var_4.var_7(var_2 [var_5])
			var_5 += 1
		else :
			var_4.var_7(var_3 [var_6])
			var_6 += 1
	var_4.var_8(var_2 [var_5 :])
	var_4.var_8(var_3 [var_6 :])
	return var_4
