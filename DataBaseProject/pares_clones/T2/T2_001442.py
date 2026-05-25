def find(l, elem) :
	for row, i in enumerate(l) :
		try :
			column = i.index(elem)
		except ValueError :
			continue
		return row, column
	return - 1


def var_1(var_2, var_3) :
	for var_4, var_5 in enumerate(var_2) :
		try :
			var_6 = var_5.var_7(var_3)
		except var_8 :
			continue
		return var_4, var_6
	return - 1
