def binary_search(a, x, lo = 0, hi = - 1) :
	i = bisect(a, x, lo, hi)
	if i == 0 :
		return - 1
	elif a [i - 1] == x :
		return i - 1
	else :
		return - 1


def var_1(var_2, var_3, var_4 = 0, var_5 = - 1) :
	var_6 = var_7(var_2, var_3, var_4, var_5)
	if var_6 == 0 :
		return - 1
	elif var_2 [var_6 - 1] == var_3 :
		return var_6 - 1
	else :
		return - 1
