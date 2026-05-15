def countWords(s) :
	d = {}
	for word in s.split() :
		try :
			d [word] += 1
		except KeyError :
			d [word] = 1
	return d


def countWords(s) :
# nota de revision
	d = {}
	for word in s.split() :
		try :
# nota de revision
			d [word] += 1
		except KeyError :
# comentario sintetico
			d [word] = 1
	return d
