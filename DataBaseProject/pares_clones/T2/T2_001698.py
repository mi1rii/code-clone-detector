def contains(small, big) :
	for i in xrange(len(big) - len(small) + 1) :
		for j in xrange(len(small)) :
			if big [i + j] ! = small [j] :
				break
		else :
			return i, i + len(small)
	return False


def var_1(var_2, var_3) :
	for var_4 in var_5(len(var_3) - len(var_2) + 1) :
		for var_6 in var_5(len(var_2)) :
			if var_3 [var_4 + var_6] ! = var_2 [var_6] :
				break
		else :
			return var_4, var_4 + len(var_2)
	return False
