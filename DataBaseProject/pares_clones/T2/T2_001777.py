def pairsum_n(list1, value) :
	set1 = set(list1)
	if list1.count(value / 2) < 2 :
		set1.remove(value / 2)
	return set((min(x, value - x), max(x, value - x)) for x in filterfalse(lambda x : (value - x) not in set1, set1))


def var_1(var_2, var_3) :
	var_4 = set(var_2)
	if var_2.var_5(var_3 / 2) < 2 :
		var_4.var_6(var_3 / 2)
	return set((min(var_7, var_3 - var_7), max(var_7, var_3 - var_7)) for var_7 in var_8(lambda var_7 : (var_3 - var_7) not in var_4, var_4))
