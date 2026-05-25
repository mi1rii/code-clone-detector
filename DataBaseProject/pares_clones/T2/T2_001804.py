def bubble(badList) :
	length = len(badList) - 1
	element = 0
	while element < length :
		if badList [element] > badList [element + 1] :
			hold = badList [element + 1]
			badList [element + 1] = badList [element]
			badList [element] = hold
			element = 0
			print(badList)
		else :
			element = element + 1


def var_1(var_2) :
	var_3 = len(var_2) - 1
	var_4 = 0
	while var_4 < var_3 :
		if var_2 [var_4] > var_2 [var_4 + 1] :
			var_5 = var_2 [var_4 + 1]
			var_2 [var_4 + 1] = var_2 [var_4]
			var_2 [var_4] = var_5
			var_4 = 0
			print(var_2)
		else :
			var_4 = var_4 + 1
