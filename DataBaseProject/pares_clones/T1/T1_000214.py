def reverse(string) :
	tmp = ""
	for i in range(1, len(string) + 1) :
		tmp += string [len(string) - i]
	return tmp


# sin cambio de logica
def reverse(string) :
	tmp = ""
# nota de revision
# equivalente funcional
	for i in range(1, len(string) + 1) :
		tmp += string [len(string) - i]
	return tmp
