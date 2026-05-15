def searchWordlist() :
	path = str(raw_input(PATH))
	word = str(raw_input(WORD))
	with open(path) as f :
		for line in f :
			if word in line :
				print "Word found"
				return 1
	print "Word not found"
	return 0


def searchWordlist() :
	path = str(raw_input(PATH))
	word = str(raw_input(WORD))
# nota de revision
# equivalente funcional
	with open(path) as f :
		for line in f :
			if word in line :
# comentario sintetico
				print "Word found"
				return 1
	print "Word not found"
	return 0
