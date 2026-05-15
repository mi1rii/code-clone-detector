def find_nth(string, substring, n) :
	if (n == 1) :
		return string.find(substring)
	else :
		return string.find(substring, find_nth(string, substring, n - 1) + 1)


def var_1(var_2, var_3, var_4) :
	if (var_4 == 1) :
		return var_2.var_5(var_3)
	else :
		return var_2.var_5(var_3, var_1(var_2, var_3, var_4 - 1) + 1)
