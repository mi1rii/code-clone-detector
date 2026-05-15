def minimum(lst, current_min = None) :
	if not lst :
		return current_min
	if current_min is None :
		current_min = lst [0]
	elif lst [0] < current_min :
		current_min = lst [0]
	return minimum(lst [1 :], current_min)


def var_1(var_2, var_3 = None) :
	if not var_2 :
		return var_3
	if var_3 is None :
		var_3 = var_2 [0]
	elif var_2 [0] < var_3 :
		var_3 = var_2 [0]
	return var_1(var_2 [1 :], var_3)
