def merge_sort(data) :
	if len(data) == 1 :
		return data
	middle = len(data) / / 2
	left_data = merge_sort(data [: middle])
	right_data = merge_sort(data [middle :])
	return merge(left_data, right_data)


def var_1(var_2) :
	if len(var_2) == 1 :
		return var_2
	var_3 = len(var_2) / / 2
	var_4 = var_1(var_2 [: var_3])
	var_5 = var_1(var_2 [var_3 :])
	return var_6(var_4, var_5)
