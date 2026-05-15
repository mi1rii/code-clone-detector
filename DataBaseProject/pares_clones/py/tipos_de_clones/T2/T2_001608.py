def contains_consecutive_duplicates(xs) :
	for i in xs :
		if xs.indexOf(i) == len(xs) :
			break
		if xs [i] == xs [i - 1] or xs [i] == xs [i + 1] :
			return True
		else :
			return False


def var_1(var_2) :
	for var_3 in var_2 :
		if var_2.var_4(var_3) == len(var_2) :
			break
		if var_2 [var_3] == var_2 [var_3 - 1] or var_2 [var_3] == var_2 [var_3 + 1] :
			return True
		else :
			return False
