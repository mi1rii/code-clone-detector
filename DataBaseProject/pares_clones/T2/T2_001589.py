def json_scan(json_obj, key) :
	d = json.loads(json_obj)
	for k in d:
		if k == key:
			return d[key]


def var_1(var_2, var_3) :
	var_4 = var_5.var_6(var_2)
	for var_7 in var_4:
		if var_7 == var_3:
			return var_4[var_3]
