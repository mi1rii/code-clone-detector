def int_to_roman(number) :
	result = ""
	for (arabic, roman) in ROMAN :
		(factor, number) = divmod(number, arabic)
		result += roman * factor
	return result


def var_1(var_2) :
	var_3 = ""
	for (var_4, var_5) in var_6 :
		(var_7, var_2) = var_8(var_2, var_4)
		var_3 += var_5 * var_7
	return var_3
