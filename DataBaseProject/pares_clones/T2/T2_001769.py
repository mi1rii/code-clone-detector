def merge_sort(x) :
	if len(x) < 2 : return x
	result, mid = [], int(len(x) / 2)
	y = merge_sort(x [: mid])
	z = merge_sort(x [mid :])
	while (len(y) > 0) and (len(z) > 0) :
		if y [0] > z [0] : result.append(z.pop(0))
		else : result.append(y.pop(0))
	result.extend(y + z)
	return result


def var_1(var_2) :
	if len(var_2) < 2 : return var_2
	var_3, var_4 = [], int(len(var_2) / 2)
	var_5 = var_1(var_2 [: var_4])
	var_6 = var_1(var_2 [var_4 :])
	while (len(var_5) > 0) and (len(var_6) > 0) :
		if var_5 [0] > var_6 [0] : var_3.var_7(var_6.var_8(0))
		else : var_3.var_7(var_5.var_8(0))
	var_3.var_9(var_5 + var_6)
	return var_3
