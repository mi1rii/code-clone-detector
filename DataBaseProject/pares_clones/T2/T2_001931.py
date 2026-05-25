def num_subsequences(seq, sub) :
	if not sub :
		return 1
	elif not seq :
		return 0
	result = num_subsequences(seq [1 :], sub)
	if seq [0] == sub [0] :
		result += num_subsequences(seq [1 :], sub [1 :])
	return result


def var_1(var_2, var_3) :
	if not var_3 :
		return 1
	elif not var_2 :
		return 0
	var_4 = var_1(var_2 [1 :], var_3)
	if var_2 [0] == var_3 [0] :
		var_4 += var_1(var_2 [1 :], var_3 [1 :])
	return var_4
