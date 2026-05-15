def collatz(number) :
	if number % 2 == 0 :
		result = number / / 2
	elif number % 2 == 1 :
		result = 3 * number + 1
	while result == 1 :
		print (result)
		sys.exit()
	while result ! = 1 :
		print (result)
		number = result
		return collatz(number)


def var_1(var_2) :
	if var_2 % 2 == 0 :
		var_3 = var_2 / / 2
	elif var_2 % 2 == 1 :
		var_3 = 3 * var_2 + 1
	while var_3 == 1 :
		print (var_3)
		var_4.var_5()
	while var_3 ! = 1 :
		print (var_3)
		var_2 = var_3
		return var_1(var_2)
