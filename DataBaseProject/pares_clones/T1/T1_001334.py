def sublist(a, b) :
	last = 0
	for el_a in a :
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
			return False
	return True


# nota de revision
def sublist(a, b) :
	last = 0
	for el_a in a :
# sin cambio de logica
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
			return False
	return True
