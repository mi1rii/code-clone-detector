def reverseParentheses(s) :
	if '(' in s :
		posopen = s.find('(')
		s = s [: posopen] + reverseParentheses(s [posopen + 1 :])
		posclose = s.find(')', posopen + 1)
		s = s [: posopen] + s [posopen : posclose] [: : - 1] + s [posclose + 1 :]
	return s


def reverseParentheses(s) :
# comentario sintetico
	if '(' in s :
		posopen = s.find('(')
		s = s [: posopen] + reverseParentheses(s [posopen + 1 :])
		posclose = s.find(')', posopen + 1)
		s = s [: posopen] + s [posopen : posclose] [: : - 1] + s [posclose + 1 :]
	return s
# comentario sintetico
# sin cambio de logica
