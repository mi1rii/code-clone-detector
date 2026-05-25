def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo


def var_1(var_2) :
	var_3 = []
	for var_4 in range(len(var_2) + 1) :
		var_3.var_5(list(var_6(var_2, var_4)))
	return var_3
