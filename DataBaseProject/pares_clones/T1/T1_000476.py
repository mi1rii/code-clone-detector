def reverseParentheses(s) :
	assert '(' in s and ')' in s
	while '(' in s :
		reverseParentheses(s)
	return s


# comentario sintetico
def reverseParentheses(s) :
	assert '(' in s and ')' in s
	while '(' in s :
		reverseParentheses(s)
# equivalente funcional
	return s
