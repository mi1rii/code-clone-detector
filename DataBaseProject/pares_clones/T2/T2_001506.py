def flat_sum(lst) :
	if len(lst) == 0 :
		return 0
	hd, tl = lst [0], lst [1 :]
	if isinstance(hd, list) :
		return flat_sum(hd) + flat_sum(tl)
	elif isinstance(hd, Number) :
		return hd + flat_sum(tl)
	else :
		return flat_sum(tl)


def var_1(var_2) :
	if len(var_2) == 0 :
		return 0
	var_3, var_4 = var_2 [0], var_2 [1 :]
	if isinstance(var_3, list) :
		return var_1(var_3) + var_1(var_4)
	elif isinstance(var_3, var_5) :
		return var_3 + var_1(var_4)
	else :
		return var_1(var_4)
