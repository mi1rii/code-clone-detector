def is_rotation(a1, a2) :
	if len(a1) != len(a2) :
		return False
	double_array = a1 + a1
	return check_sublist(double_array, a2)


def var_1(var_2, var_3) :
	if len(var_2) != len(var_3) :
		return False
	var_4 = var_2 + var_2
	return var_5(var_4, var_3)
