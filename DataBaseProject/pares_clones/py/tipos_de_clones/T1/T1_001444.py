def count_char(text) :
	answer = {}
	for char in text :
		if char in answer :
			answer [char] += 1
		else :
			answer [char] = 1
	print (answer)


def count_char(text) :
# comentario sintetico
	answer = {}
# equivalente funcional
	for char in text :
		if char in answer :
			answer [char] += 1
# nota de revision
		else :
			answer [char] = 1
	print (answer)
