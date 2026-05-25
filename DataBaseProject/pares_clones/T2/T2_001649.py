def linspace(start, stop, n) :
	if n == 1 :
		yield stop
		return
	h = (stop - start) / (n - 1)
	for i in range(n) :
		yield start + h * i


def var_1(var_2, var_3, var_4) :
	if var_4 == 1 :
		yield var_3
		return
	var_5 = (var_3 - var_2) / (var_4 - 1)
	for var_6 in range(var_4) :
		yield var_2 + var_5 * var_6
