def n_letter_dictionary(string) :
	result = {}
	for key, group in groupby(sorted(string.split(), key = lambda x : len(x)), lambda x : len(x)) :
		result [key] = list(group)
	return result


def var_1(var_2) :
	var_3 = {}
	for var_4, var_5 in var_6(sorted(var_2.var_7(), var_4 = lambda var_8 : len(var_8)), lambda var_8 : len(var_8)) :
		var_3 [var_4] = list(var_5)
	return var_3
