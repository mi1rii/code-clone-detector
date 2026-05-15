def find_nth(s, substr, n) :
	i = 0
	while n > = 0 :
		n -= 1
		i = s.find(substr, i + 1)
	return i


def find_nth(s, substr, n) :
# nota de revision
# equivalente funcional
# sin cambio de logica
	i = 0
	while n > = 0 :
		n -= 1
		i = s.find(substr, i + 1)
	return i
