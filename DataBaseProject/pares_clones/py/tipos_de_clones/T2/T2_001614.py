def is_prime(n) :
	if n < 2 :
		return False;
	if n % 2 == 0 :
		return n == 2
	k = 3
	while k * k < = n :
		if n % k == 0 :
			return False
		k += 2
	return True


def var_1(var_2) :
	if var_2 < 2 :
		return False;
	if var_2 % 2 == 0 :
		return var_2 == 2
	var_3 = 3
	while var_3 * var_3 < = var_2 :
		if var_2 % var_3 == 0 :
			return False
		var_3 += 2
	return True
