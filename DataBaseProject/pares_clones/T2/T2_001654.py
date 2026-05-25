def split_at_first_false(pred, seq) :
	if not isinstance(seq, list) :
		seq = list(seq)
	for i, x in enumerate(seq) :
		if not pred(x) :
			return seq [: i], seq [i :]
	return seq, []


def var_1(var_2, var_3) :
	if not isinstance(var_3, list) :
		var_3 = list(var_3)
	for var_4, var_5 in enumerate(var_3) :
		if not var_2(var_5) :
			return var_3 [: var_4], var_3 [var_4 :]
	return var_3, []
