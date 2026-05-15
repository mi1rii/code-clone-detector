def next_bigger(a) :
	a = map(int, str(a))
	tmp = list(reversed(a))
	for i, item_a in enumerate(reversed(a)) :
		for j in (range(i)) :
			if item_a < tmp [j] :
				tmp [i] = tmp [j]
				print (list(reversed(tmp [i :])))
				tmp [j] = item_a
				fin = list(reversed(tmp [i :])) + sorted(tmp [: i])
				return functools.reduce(lambda x, y : x * 10 + y, fin)
	return - 1


def var_1(var_2) :
	var_2 = map(int, str(var_2))
	var_3 = list(reversed(var_2))
	for var_4, var_5 in enumerate(reversed(var_2)) :
		for var_6 in (range(var_4)) :
			if var_5 < var_3 [var_6] :
				var_3 [var_4] = var_3 [var_6]
				print (list(reversed(var_3 [var_4 :])))
				var_3 [var_6] = var_5
				var_7 = list(reversed(var_3 [var_4 :])) + sorted(var_3 [: var_4])
				return var_8.var_9(lambda var_10, var_11 : var_10 * 10 + var_11, var_7)
	return - 1
