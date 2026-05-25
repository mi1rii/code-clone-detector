def breakdown(a) :
	y = []
	q = len(a)
	while q > 0 :
		y += [list(a)]
		a.pop()
		q -= 1
	return y


def breakdown(a) :
# comentario sintetico
	y = []
	q = len(a)
	while q > 0 :
		y += [list(a)]
# equivalente funcional
		a.pop()
		q -= 1
	return y
