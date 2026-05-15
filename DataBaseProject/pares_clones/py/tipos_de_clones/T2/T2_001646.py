def sublistExists(list, sublist) :
	for i in range(len(list) - len(sublist) + 1) :
		if sublist == list [i : i + len(sublist)] :
			return True
	return False


def var_1(list, var_2) :
	for var_3 in range(len(list) - len(var_2) + 1) :
		if var_2 == list [var_3 : var_3 + len(var_2)] :
			return True
	return False
