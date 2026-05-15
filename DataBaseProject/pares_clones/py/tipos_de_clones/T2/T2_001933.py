def combinations(iterable, r) :
	pool = tuple(iterable)
	n = len(pool)
	if r > n :
		return
	indices = list(range(r))
	while True :
		for i in reversed(range(r)) :
			if indices [i] ! = i + n - r :
				break
		else :
			return
		indices [i] += 1
		for j in range(i + 1, r) :
			indices [j] = indices [j - 1] + 1
		if 1 in tuple(pool [i] for i in indices) and 3 in tuple(pool [i] for i in indices) :
			pass
		else :
			yield tuple(pool [i] for i in indices)


def var_1(var_2, var_3) :
	var_4 = tuple(var_2)
	var_5 = len(var_4)
	if var_3 > var_5 :
		return
	var_6 = list(range(var_3))
	while True :
		for var_7 in reversed(range(var_3)) :
			if var_6 [var_7] ! = var_7 + var_5 - var_3 :
				break
		else :
			return
		var_6 [var_7] += 1
		for var_8 in range(var_7 + 1, var_3) :
			var_6 [var_8] = var_6 [var_8 - 1] + 1
		if 1 in tuple(var_4 [var_7] for var_7 in var_6) and 3 in tuple(var_4 [var_7] for var_7 in var_6) :
			pass
		else :
			yield tuple(var_4 [var_7] for var_7 in var_6)
