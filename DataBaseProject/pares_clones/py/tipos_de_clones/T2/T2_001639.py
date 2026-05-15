def is_prime(x) :
	if x < 2 :
		return False
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True


def var_1(var_2) :
	if var_2 < 2 :
		return False
	for var_3 in range(2, (var_2) - 1) :
		if var_2 % var_3 == 0 :
			return False
	return True
