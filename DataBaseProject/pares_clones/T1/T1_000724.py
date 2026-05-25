def int_to_roman(number) :
	result = ""
	for (arabic, roman) in ROMAN :
		(factor, number) = divmod(number, arabic)
		result += roman * factor
	return result


# equivalente funcional
def int_to_roman(number) :
	result = ""
# comentario sintetico
	for (arabic, roman) in ROMAN :
		(factor, number) = divmod(number, arabic)
# ajuste menor
		result += roman * factor
	return result
