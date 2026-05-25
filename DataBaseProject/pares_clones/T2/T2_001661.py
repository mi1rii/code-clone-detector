def paren(n, known = {}) :
	if n in known :
		return known [n]
	ps = set(['(' * n + ')' * n])
	for i in range(1, n) :
		for f in paren(i, known) :
			for s in paren(n - i, known) :
				ps.add(f + s)
	known [n] = ps
	return ps


def var_1(var_2, var_3 = {}) :
	if var_2 in var_3 :
		return var_3 [var_2]
	var_4 = set(['(' * var_2 + ')' * var_2])
	for var_5 in range(1, var_2) :
		for var_6 in var_1(var_5, var_3) :
			for var_7 in var_1(var_2 - var_5, var_3) :
				var_4.var_8(var_6 + var_7)
	var_3 [var_2] = var_4
	return var_4
