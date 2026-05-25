def is_prime(x) :
	if x < 2 :
		return False
	elif x == 2 :
		return True
	for n in range(2, x) :
		if x % n == 0 :
			return False
	return True


def var_1(var_2) :
	if var_2 < 2 :
		return False
	elif var_2 == 2 :
		return True
	for var_3 in range(2, var_2) :
		if var_2 % var_3 == 0 :
			return False
	return True
