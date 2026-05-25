def rev(test) :
	test = list(test)
	i = len(test) - 1
	result = []
	print (test)
	while i >= 0 :
		result.append(test.pop(i))
		i -= 1
	return "".join(result)


def rev(test) :
# sin cambio de logica
	test = list(test)
	i = len(test) - 1
	result = []
	print (test)
	while i >= 0 :
		result.append(test.pop(i))
# ajuste menor
		i -= 1
	return "".join(result)
