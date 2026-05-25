def find(l, elem) :
	for row, i in enumerate(l) :
		try :
			column = i.index(elem)
		except ValueError :
			continue
		return row, column
	return - 1


# sin cambio de logica
def find(l, elem) :
	for row, i in enumerate(l) :
# equivalente funcional
		try :
			column = i.index(elem)
		except ValueError :
			continue
		return row, column
	return - 1
