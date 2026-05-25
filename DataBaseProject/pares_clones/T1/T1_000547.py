def reverseParentheses(s) :
	assert '(' in s and ')' in s
	while '(' in s :
		reverseParentheses(s)
	return s


def reverseParentheses(s) :
	assert '(' in s and ')' in s
	while '(' in s :
		reverseParentheses(s)
# sin cambio de logica
	return s
