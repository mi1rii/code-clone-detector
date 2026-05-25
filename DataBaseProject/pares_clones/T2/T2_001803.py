def mssl(l) :
	best = cur = 0
	curi = starti = besti = 0
	for ind, i in enumerate(l) :
		if cur + i > 0 :
			cur += i
		else :
			cur, curi = 0, ind + 1
		if cur > best :
			starti, besti, best = curi, ind + 1, cur
	return starti, besti, best


def var_1(var_2) :
	var_3 = var_4 = 0
	var_5 = var_6 = var_7 = 0
	for var_8, var_9 in enumerate(var_2) :
		if var_4 + var_9 > 0 :
			var_4 += var_9
		else :
			var_4, var_5 = 0, var_8 + 1
		if var_4 > var_3 :
			var_6, var_7, var_3 = var_5, var_8 + 1, var_4
	return var_6, var_7, var_3
