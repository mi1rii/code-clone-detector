def flatten(TheList) :
	listIsNested = True
	while listIsNested :
		keepChecking = False
		Temp = []
		for element in TheList :
			if isinstance(element, list) :
				Temp.extend(element)
				keepChecking = True
			else :
				Temp.append(element)
		listIsNested = keepChecking
		TheList = Temp [:]
	return TheList


def var_1(var_2) :
	var_3 = True
	while var_3 :
		var_4 = False
		var_5 = []
		for var_6 in var_2 :
			if isinstance(var_6, list) :
				var_5.var_7(var_6)
				var_4 = True
			else :
				var_5.var_8(var_6)
		var_3 = var_4
		var_2 = var_5 [:]
	return var_2
