def mergeSort(L, compare = operator.lt) :
	if len(L) < 2 :
		return L [:]
	else :
		middle = int(len(L) / 2)
		left = mergeSort(L [: middle], compare)
		right = mergeSort(L [middle :], compare)
		return merge(left, right, compare)


def var_1(var_2, var_3 = var_4.var_5) :
	if len(var_2) < 2 :
		return var_2 [:]
	else :
		var_6 = int(len(var_2) / 2)
		var_7 = var_1(var_2 [: var_6], var_3)
		var_8 = var_1(var_2 [var_6 :], var_3)
		return var_9(var_7, var_8, var_3)
