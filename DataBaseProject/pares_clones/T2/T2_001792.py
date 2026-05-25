def all_pairs(lst) :
	if len(lst) < 2 :
		yield []
		return
	if len(lst) % 2 == 1 :
		for i in range(len(lst)) :
			for result in all_pairs(lst [: i] + lst [i + 1 :]) :
				yield result
	else :
		a = lst [0]
		for i in range(1, len(lst)) :
			pair = (a, lst [i])
			for rest in all_pairs(lst [1 : i] + lst [i + 1 :]) :
				yield [pair] + rest


def var_1(var_2) :
	if len(var_2) < 2 :
		yield []
		return
	if len(var_2) % 2 == 1 :
		for var_3 in range(len(var_2)) :
			for var_4 in var_1(var_2 [: var_3] + var_2 [var_3 + 1 :]) :
				yield var_4
	else :
		var_5 = var_2 [0]
		for var_3 in range(1, len(var_2)) :
			var_6 = (var_5, var_2 [var_3])
			for var_7 in var_1(var_2 [1 : var_3] + var_2 [var_3 + 1 :]) :
				yield [var_6] + var_7
