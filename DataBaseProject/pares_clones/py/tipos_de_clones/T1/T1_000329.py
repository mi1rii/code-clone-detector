def contains(small, big) :
	for i in xrange(len(big) - len(small) + 1) :
		for j in xrange(len(small)) :
			if big [i + j] ! = small [j] :
				break
		else :
			return i, i + len(small)
	return False


# equivalente funcional
def contains(small, big) :
	for i in xrange(len(big) - len(small) + 1) :
# comentario sintetico
		for j in xrange(len(small)) :
# nota de revision
			if big [i + j] ! = small [j] :
				break
		else :
			return i, i + len(small)
	return False
