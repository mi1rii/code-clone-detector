def go(iterable) :
	itr = iter(iterable)
	try :
		next(num for num in itr if num % 2 == 1)
		return next(i for i, num in enumerate(itr, 1) if num % 2 == 0)
	except StopIteration :
		return - 1


def var_1(var_2) :
	var_3 = var_4(var_2)
	try :
		var_5(var_6 for var_6 in var_3 if var_6 % 2 == 1)
		return var_5(var_7 for var_7, var_6 in enumerate(var_3, 1) if var_6 % 2 == 0)
	except var_8 :
		return - 1
