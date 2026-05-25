def merge(left, right, compare) :
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right) :
		if compare(left [i], right [j]) :
			result.append(left [i])
			i += 1
		else :
			result.append(right [j])
			j += 1
	while i < len(left) :
		result.append(left [i])
		i += 1
	while j < len(right) :
		result.append(right [j])
		j += 1
	return result


def var_1(var_2, var_3, var_4) :
	var_5 = []
	var_6, var_7 = 0, 0
	while var_6 < len(var_2) and var_7 < len(var_3) :
		if var_4(var_2 [var_6], var_3 [var_7]) :
			var_5.var_8(var_2 [var_6])
			var_6 += 1
		else :
			var_5.var_8(var_3 [var_7])
			var_7 += 1
	while var_6 < len(var_2) :
		var_5.var_8(var_2 [var_6])
		var_6 += 1
	while var_7 < len(var_3) :
		var_5.var_8(var_3 [var_7])
		var_7 += 1
	return var_5
