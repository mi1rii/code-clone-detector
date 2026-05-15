def minimum(lst) :
	if len(lst) == 1 :
		return lst [0]
	first = lst [0]
	rest = lst [1 :]
	min_of_rest = minimum(rest)
	if first < min_of_rest :
		return first
	else :
		return min_of_rest


def var_1(var_2) :
	if len(var_2) == 1 :
		return var_2 [0]
	var_3 = var_2 [0]
	var_4 = var_2 [1 :]
	var_5 = var_1(var_4)
	if var_3 < var_5 :
		return var_3
	else :
		return var_5
