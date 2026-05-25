def neclusters(l, K) :
	for splits in itertools.combinations(range(len(l) - 1), K - 1) :
		splits = [0] + [s + 1 for s in splits] + [None]
		yield [l [s : e] for s, e in zip(splits, splits [1 :])]


def var_1(var_2, var_3) :
	for var_4 in var_5.var_6(range(len(var_2) - 1), var_3 - 1) :
		var_4 = [0] + [var_7 + 1 for var_7 in var_4] + [None]
		yield [var_2 [var_7 : var_8] for var_7, var_8 in zip(var_4, var_4 [1 :])]
