def split_at_first_false(pred, seq) :
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]


def var_1(var_2, var_3) :
	for var_4, var_5 in enumerate(var_3) :
		if not var_2(var_5) :
			return var_3 [: var_4], var_3 [var_4 :]
