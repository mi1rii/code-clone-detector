def numPens(n) :
	if n < 5 :
		return False
	elif n == 5 or n == 8 or n == 24 :
		return True
	else :
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)


def var_1(var_2) :
	if var_2 < 5 :
		return False
	elif var_2 == 5 or var_2 == 8 or var_2 == 24 :
		return True
	else :
		return var_1(var_2 - 5) or var_1(var_2 - 8) or var_1(var_2 - 24)
