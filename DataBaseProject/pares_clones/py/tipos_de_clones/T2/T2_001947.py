def merge_sort(sequence) :
	if len(sequence) < 2 :
		return sequence
	mid = len(sequence) / / 2
	left_sequence = merge_sort(sequence [: mid])
	right_sequence = merge_sort(sequence [mid :])
	return merge(left_sequence, right_sequence)


def var_1(var_2) :
	if len(var_2) < 2 :
		return var_2
	var_3 = len(var_2) / / 2
	var_4 = var_1(var_2 [: var_3])
	var_5 = var_1(var_2 [var_3 :])
	return var_6(var_4, var_5)
