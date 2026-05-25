def printFigure(rows) :
	for x in range(rows) :
		items = [str(i) for i in range(1, x + 1)]
		if x % 2 == 0 :
			items = items [: : - 1]
		print (''.join(items))


def var_1(var_2) :
	for var_3 in range(var_2) :
		var_4 = [str(var_5) for var_5 in range(1, var_3 + 1)]
		if var_3 % 2 == 0 :
			var_4 = var_4 [: : - 1]
		print (''.var_6(var_4))
