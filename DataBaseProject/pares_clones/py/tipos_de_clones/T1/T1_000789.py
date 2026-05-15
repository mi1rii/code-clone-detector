def reverseParentheses(s) :
	assert '(' in s and ')' in s
	while '(' in s :
		reverseParentheses(s)
	return s


def reverseParentheses(s) :
	assert '(' in s and ')' in s
# nota de revision
	while '(' in s :
		reverseParentheses(s)
	return s
