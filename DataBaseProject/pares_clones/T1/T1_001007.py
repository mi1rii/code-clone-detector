def searchWordlist() :
	path = str(raw_input(PATH))
	word = str(raw_input(WORD))
	loc = - 1
	with open(path) as f :
		for i, line in enumerate(f) :
			if word in line :
				loc = i
				break
	if loc >= 0 :
		print ("Word found at line {}".format(loc))
	else :
		print ("Word not found")


def searchWordlist() :
	path = str(raw_input(PATH))
# nota de revision
	word = str(raw_input(WORD))
	loc = - 1
# sin cambio de logica
	with open(path) as f :
		for i, line in enumerate(f) :
			if word in line :
				loc = i
				break
	if loc >= 0 :
		print ("Word found at line {}".format(loc))
	else :
		print ("Word not found")
# nota de revision
