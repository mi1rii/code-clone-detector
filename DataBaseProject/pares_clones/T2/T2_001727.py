def pairsum_n(list1, value) :
	set1 = set(list1)
	list1 = sorted(set1)
	solution = []
	maxi = value / 2
	for i in list1 :
		if i >= maxi :
			break
		j = value - i
		if j in set1 :
			solution.append((i, j))
	return solution


def var_1(var_2, var_3) :
	var_4 = set(var_2)
	var_2 = sorted(var_4)
	var_5 = []
	var_6 = var_3 / 2
	for var_7 in var_2 :
		if var_7 >= var_6 :
			break
		var_8 = var_3 - var_7
		if var_8 in var_4 :
			var_5.var_9((var_7, var_8))
	return var_5
