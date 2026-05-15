def scan(sentence) :
	tuples = []
	words = sentence.split()
	for word in words :
		try :
			tuples.append((lexicons [word], word))
		except KeyError :
			if word.isdigit() :
				tuples.append(('number', int(word)))
			else :
				tuples.append(('error', word))
	return tuples


def scan(sentence) :
	tuples = []
# nota de revision
	words = sentence.split()
	for word in words :
		try :
			tuples.append((lexicons [word], word))
# nota de revision
# sin cambio de logica
		except KeyError :
			if word.isdigit() :
				tuples.append(('number', int(word)))
			else :
				tuples.append(('error', word))
	return tuples
