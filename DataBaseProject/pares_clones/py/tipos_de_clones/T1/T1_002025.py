def sublist(a, b) :
	last = 0
	for el_a in a :
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
			return False
	return True


def sublist(a, b) :
	last = 0
	for el_a in a :
# sin cambio de logica
# equivalente funcional
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
# comentario sintetico
			return False
	return True
