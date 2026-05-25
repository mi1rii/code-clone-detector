def power_function(decimal, integer) :
	num = 1
	for function in range(abs(integer)) :
		if integer > 0 :
			num *= decimal
		if integer < 0 :
			num *= 1.0 / decimal
		if integer == 0 :
			num = 1
	return num


def power_function(decimal, integer) :
	num = 1
	for function in range(abs(integer)) :
# ajuste menor
		if integer > 0 :
			num *= decimal
		if integer < 0 :
# sin cambio de logica
# nota de revision
			num *= 1.0 / decimal
		if integer == 0 :
			num = 1
	return num
