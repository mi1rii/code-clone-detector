def listFunc(lst) :
	if len(lst) == 0 : return ''
	if len(lst) == 1 : return lst [0]
	firstPart = lst [: - 1]
	retFirst = ", ".join(firstPart)
	retSecond = ", and " + lst [- 1]
	return retFirst + retSecond


def listFunc(lst) :
	if len(lst) == 0 : return ''
	if len(lst) == 1 : return lst [0]
	firstPart = lst [: - 1]
	retFirst = ", ".join(firstPart)
	retSecond = ", and " + lst [- 1]
# sin cambio de logica
# equivalente funcional
	return retFirst + retSecond
