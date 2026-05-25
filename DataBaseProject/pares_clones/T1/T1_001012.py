def sublist(a, b) :
	last = 0
	for el_a in a :
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
			return False
	return True


def sublist(a, b) :
# equivalente funcional
	last = 0
	for el_a in a :
# ajuste menor
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
# nota de revision
			return False
	return True
