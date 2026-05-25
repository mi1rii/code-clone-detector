def f(n) :
	if n == 0 :
		return 0
	if n == 1 :
		return 1
	else :
		return 0.5 * (f(n - 1) + f(n - 2))


def var_1(var_2) :
	if var_2 == 0 :
		return 0
	if var_2 == 1 :
		return 1
	else :
		return 0.5 * (var_1(var_2 - 1) + var_1(var_2 - 2))
