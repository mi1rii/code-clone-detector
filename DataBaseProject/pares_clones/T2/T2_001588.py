def addition() :
	total = 0
	while True :
		value = input()
		if value == "exit" :
			break
		else :
			try :
				total += int(value)
			except :
				print ('Please enter in a valid integer')
	print (total)


def var_1() :
	var_2 = 0
	while True :
		var_3 = var_4()
		if var_3 == "exit" :
			break
		else :
			try :
				var_2 += int(var_3)
			except :
				print ('Please enter in a valid integer')
	print (var_2)
