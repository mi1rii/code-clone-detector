def same_structure(a, b) :
	if a == [] or b == [] :
		return a == b
	elif is_list(a [0]) ! = is_list(b [0]) :
		return False
	elif not is_list(a [0]) :
		return same_structure(a [1 :], b [1 :])
	else :
		return same_structure(a [0], b [0]) and same_structure(a [1 :], b [1 :])


def var_1(var_2, var_3) :
	if var_2 == [] or var_3 == [] :
		return var_2 == var_3
	elif var_4(var_2 [0]) ! = var_4(var_3 [0]) :
		return False
	elif not var_4(var_2 [0]) :
		return var_1(var_2 [1 :], var_3 [1 :])
	else :
		return var_1(var_2 [0], var_3 [0]) and var_1(var_2 [1 :], var_3 [1 :])
