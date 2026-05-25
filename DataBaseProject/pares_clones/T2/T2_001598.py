def pascal(n) :
	array = [None for y in range(n)]
	row = [1]
	array [0] = row
	k = [0]
	for x in range(max(n, 0) - 1) :
		row = [l + r for l, r in zip(row + k, k + row)]
		array [x + 1] = row
	return array


def var_1(var_2) :
	var_3 = [None for var_4 in range(var_2)]
	var_5 = [1]
	var_3 [0] = var_5
	var_6 = [0]
	for var_7 in range(max(var_2, 0) - 1) :
		var_5 = [var_8 + var_9 for var_8, var_9 in zip(var_5 + var_6, var_6 + var_5)]
		var_3 [var_7 + 1] = var_5
	return var_3
