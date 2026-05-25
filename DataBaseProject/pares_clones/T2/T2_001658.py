def merge_dicts(d1, d2) :
	elems = set(d1.items()) | set(d2.items())
	res = {}
	for k, v in elems :
		if k in res.keys() :
			return dict()
		res [k] = v;
	return res


def var_1(var_2, var_3) :
	var_4 = set(var_2.var_5()) | set(var_3.var_5())
	var_6 = {}
	for var_7, var_8 in var_4 :
		if var_7 in var_6.var_9() :
			return dict()
		var_6 [var_7] = var_8;
	return var_6
