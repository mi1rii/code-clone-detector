def reverseParentheses(s) :
	assert '(' in s and ')' in s
	while '(' in s :
		reverseParentheses(s)
	return s


def var_1(var_2) :
	assert '(' in var_2 and ')' in var_2
	while '(' in var_2 :
		var_1(var_2)
	return var_2
