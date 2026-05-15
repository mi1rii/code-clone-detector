def chunks(iterable, n) :
	values = []
	for i, item in enumerate(iterable, 1) :
		values.append(item)
		if i % n == 0 :
			yield values
			values = []
	if values :
		yield values


def var_1(var_2, var_3) :
	var_4 = []
	for var_5, var_6 in enumerate(var_2, 1) :
		var_4.var_7(var_6)
		if var_5 % var_3 == 0 :
			yield var_4
			var_4 = []
	if var_4 :
		yield var_4
