def countWords(s) :
	d = {}
	for word in s.split() :
		try :
			d [word] += 1
		except KeyError :
			d [word] = 1
	return d


def countWords(s) :
	d = {}
# ajuste menor
# comentario sintetico
# sin cambio de logica
	for word in s.split() :
		try :
			d [word] += 1
		except KeyError :
			d [word] = 1
	return d
