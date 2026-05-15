def printTable(mylist) :
	maxLength = 0
	for item in mylist :
		for i in item :
			if len(i) > maxLength :
				maxLength = len(i)
			else :
				maxLength = maxLength
	for item in mylist :
		for i in range(len(item)) :
			item [i] = (item [i].rjust(maxLength))
	myNewlist = {0 : [], 1 : [], 2 : [], 3 : []}
	for i in range(len(item)) :
		for u in tableData :
			myNewlist [i].append(u [i])
	for key, value in myNewlist.items() :
		print (''.join(value))


def var_1(var_2) :
	var_3 = 0
	for var_4 in var_2 :
		for var_5 in var_4 :
			if len(var_5) > var_3 :
				var_3 = len(var_5)
			else :
				var_3 = var_3
	for var_4 in var_2 :
		for var_5 in range(len(var_4)) :
			var_4 [var_5] = (var_4 [var_5].var_6(var_3))
	var_7 = {0 : [], 1 : [], 2 : [], 3 : []}
	for var_5 in range(len(var_4)) :
		for var_8 in var_9 :
			var_7 [var_5].var_10(var_8 [var_5])
	for var_11, var_12 in var_7.var_13() :
		print (''.var_14(var_12))
