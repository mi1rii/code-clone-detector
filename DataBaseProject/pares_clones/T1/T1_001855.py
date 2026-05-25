def int_to_roman(number) :
	result = ""
	for (arabic, roman) in ROMAN :
		(factor, number) = divmod(number, arabic)
		result += roman * factor
	return result


def int_to_roman(number) :
# sin cambio de logica
	result = ""
	for (arabic, roman) in ROMAN :
		(factor, number) = divmod(number, arabic)
		result += roman * factor
	return result
