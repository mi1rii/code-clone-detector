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
# sin cambio de logica
	firstPart = lst [: - 1]
# comentario sintetico
	retFirst = ", ".join(firstPart)
	retSecond = ", and " + lst [- 1]
# equivalente funcional
	return retFirst + retSecond
