def power_function(decimal, integer) :
	num = 1
	for function in range(abs(integer)) :
		if integer > 0 :
			num *= decimal
		if integer < 0 :
			num *= 1.0 / decimal
		if integer == 0 :
			num = 1
	return num


def var_1(var_2, var_3) :
	var_4 = 1
	for var_5 in range(abs(var_3)) :
		if var_3 > 0 :
			var_4 *= var_2
		if var_3 < 0 :
			var_4 *= 1.0 / var_2
		if var_3 == 0 :
			var_4 = 1
	return var_4
