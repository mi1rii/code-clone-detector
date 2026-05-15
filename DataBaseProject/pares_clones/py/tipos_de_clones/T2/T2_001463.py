def sum_even(a, b) :
	if (a % 2 == 1) :
		a += 1
	if (b % 2 == 1) :
		b -= 1
	return a * (0.5 - 0.25 * a) + b * (0.25 * b + 0.5)


def var_1(var_2, var_3) :
	if (var_2 % 2 == 1) :
		var_2 += 1
	if (var_3 % 2 == 1) :
		var_3 -= 1
	return var_2 * (0.5 - 0.25 * var_2) + var_3 * (0.25 * var_3 + 0.5)
