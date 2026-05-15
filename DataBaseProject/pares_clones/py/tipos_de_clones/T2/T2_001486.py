def is_less(a, b) :
	i = 0
	while i < len(a) :
		if a [i] < b [i] :
			return True
		else :
			if a [i] > b [i] :
				return False
		i += 1
	return False


def var_1(var_2, var_3) :
	var_4 = 0
	while var_4 < len(var_2) :
		if var_2 [var_4] < var_3 [var_4] :
			return True
		else :
			if var_2 [var_4] > var_3 [var_4] :
				return False
		var_4 += 1
	return False
