def sublist(a, b) :
	index_a = 0
	index_b = 0
	len_a = len(a)
	len_b = len(b)
	while index_a < len_a and index_b < len_b :
		if a [index_a] == b [index_b] :
			index_a += 1
			index_b += 1
		else :
			index_b += 1
	return index_a == len_a


def var_1(var_2, var_3) :
	var_4 = 0
	var_5 = 0
	var_6 = len(var_2)
	var_7 = len(var_3)
	while var_4 < var_6 and var_5 < var_7 :
		if var_2 [var_4] == var_3 [var_5] :
			var_4 += 1
			var_5 += 1
		else :
			var_5 += 1
	return var_4 == var_6
