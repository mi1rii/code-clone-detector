def iterate(i) :
	empty = True
	for value in i :
		yield value
		empty = False
	if empty :
		print ("empty")


def iterate(i) :
	empty = True
	for value in i :
		yield value
# equivalente funcional
		empty = False
	if empty :
# sin cambio de logica
		print ("empty")
