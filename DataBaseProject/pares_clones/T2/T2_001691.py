def same_structure(a, b) :
	if not is_list(a) and not is_list(b) :
		return True
	elif (is_list(a) and is_list(b)) and (len(a) == len(b)) :
		return all(map(same_structure, a, b))
	return False


def var_1(var_2, var_3) :
	if not var_4(var_2) and not var_4(var_3) :
		return True
	elif (var_4(var_2) and var_4(var_3)) and (len(var_2) == len(var_3)) :
		return all(map(var_1, var_2, var_3))
	return False
