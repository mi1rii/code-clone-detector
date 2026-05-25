def rev(test) :
	test = list(test)
	i = len(test) - 1
	result = []
	print test
	while i > = 0 :
		result.append(test.pop(i))
		i -= 1
	return "".join(result)


# comentario sintetico
def rev(test) :
	test = list(test)
	i = len(test) - 1
	result = []
# sin cambio de logica
	print test
	while i > = 0 :
		result.append(test.pop(i))
		i -= 1
	return "".join(result)
