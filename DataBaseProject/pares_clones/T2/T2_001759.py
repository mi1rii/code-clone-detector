def is_rotation(a, b) :
	for n in range(len(a)) :
		c = c = a [- n :] + a [: - n]
		if b == c :
			return True
	return False


def var_1(var_2, var_3) :
	for var_4 in range(len(var_2)) :
		var_5 = var_5 = var_2 [- var_4 :] + var_2 [: - var_4]
		if var_3 == var_5 :
			return True
	return False
