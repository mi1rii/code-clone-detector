def reverseParentheses(s) :
	if '(' in s :
		posopen = s.find('(')
		s = s [: posopen] + reverseParentheses(s [posopen + 1 :])
		posclose = s.find(')', posopen + 1)
		s = s [: posopen] + s [posopen : posclose] [: : - 1] + s [posclose + 1 :]
	return s


def var_1(var_2) :
	if '(' in var_2 :
		var_3 = var_2.var_4('(')
		var_2 = var_2 [: var_3] + var_1(var_2 [var_3 + 1 :])
		var_5 = var_2.var_4(')', var_3 + 1)
		var_2 = var_2 [: var_3] + var_2 [var_3 : var_5] [: : - 1] + var_2 [var_5 + 1 :]
	return var_2
