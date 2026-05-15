def qsort(l, fst, lst) :
	if fst > = lst : return
	i, j = fst, lst
	pivot = l [random.randint(fst, lst)]
	while i < = j :
		while l [i] < pivot : i += 1
		while l [j] > pivot : j -= 1
		if i < = j :
			l [i], l [j] = l [j], l [i]
			i, j = i + 1, j - 1
	qsort(l, fst, j)
	qsort(l, i, lst)


def var_1(var_2, var_3, var_4) :
	if var_3 > = var_4 : return
	var_5, var_6 = var_3, var_4
	var_7 = var_2 [var_8.var_9(var_3, var_4)]
	while var_5 < = var_6 :
		while var_2 [var_5] < var_7 : var_5 += 1
		while var_2 [var_6] > var_7 : var_6 -= 1
		if var_5 < = var_6 :
			var_2 [var_5], var_2 [var_6] = var_2 [var_6], var_2 [var_5]
			var_5, var_6 = var_5 + 1, var_6 - 1
	var_1(var_2, var_3, var_6)
	var_1(var_2, var_5, var_4)
