def reverse(string) :
	tmp = ""
	for i in range(1, len(string) + 1) :
		tmp += string [len(string) - i]
	return tmp


# equivalente funcional
def reverse(string) :
	tmp = ""
# ajuste menor
# nota de revision
	for i in range(1, len(string) + 1) :
		tmp += string [len(string) - i]
	return tmp
