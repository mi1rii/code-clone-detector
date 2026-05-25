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


def var_1() :
	var_2 = str(var_3(var_4))
	var_5 = str(var_3(var_6))
	with var_7(var_2) as var_8 :
		for var_9 in var_8 :
			if var_5 in var_9 :
				print "Word found"
				return 1
	print "Word not found"
	return 0
