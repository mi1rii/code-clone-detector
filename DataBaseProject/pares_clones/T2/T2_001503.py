def split_at_first_false(pred, seq) :
	index = 0
	while index < len(seq) :
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
		index += 1


def var_1(var_2, var_3) :
	var_4 = 0
	while var_4 < len(var_3) :
		if not var_2(var_3 [var_4]) :
			return var_3 [: var_4], var_3 [var_4 + 1 :]
		var_4 += 1
