def searchWordlist() :
	path = str(raw_input(PATH))
	word = str(raw_input(WORD))
	loc = - 1
	with open(path) as f :
		for i, line in enumerate(f) :
			if word in line :
				loc = i
				break
	if loc > = 0 :
		print ("Word found at line {}".format(loc))
	else :
		print ("Word not found")


def var_1() :
	var_2 = str(var_3(var_4))
	var_5 = str(var_3(var_6))
	var_7 = - 1
	with var_8(var_2) as var_9 :
		for var_10, var_11 in enumerate(var_9) :
			if var_5 in var_11 :
				var_7 = var_10
				break
	if var_7 > = 0 :
		print ("Word found at line {}".var_12(var_7))
	else :
		print ("Word not found")
