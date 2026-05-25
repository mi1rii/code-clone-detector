def base_and_num(number, base) :
	number = int(number)
	while number != 0 :
		digit = number % 10
		if digit > base :
			return False
		number = number / 10
	return True


def var_1(var_2, var_3) :
	var_2 = int(var_2)
	while var_2 != 0 :
		var_4 = var_2 % 10
		if var_4 > var_3 :
			return False
		var_2 = var_2 / 10
	return True
