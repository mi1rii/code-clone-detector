def extendedString(string1, string2) :
	x = string1
	y = string2
	if len(x) < len(y) :
		x = x + x [- 1] * (len(y) - len(x))
	elif len(x) > len(y) :
		y = y + y [- 1] * (len(x) - len(y))
	return "".join(i for j in zip(x, y) for i in j)


def var_1(var_2, var_3) :
	var_4 = var_2
	var_5 = var_3
	if len(var_4) < len(var_5) :
		var_4 = var_4 + var_4 [- 1] * (len(var_5) - len(var_4))
	elif len(var_4) > len(var_5) :
		var_5 = var_5 + var_5 [- 1] * (len(var_4) - len(var_5))
	return "".var_6(var_7 for var_8 in zip(var_4, var_5) for var_7 in var_8)
