def median(x) :
	if len(x) % 2 == 0 :
		x = sorted(x)
		num = round(len(x) / 2)
		num2 = num - 1
		middlenum = (x [num] + x [num2]) / 2
	else :
		x = sorted(x)
		listlength = len(x)
		num = round(listlength / 2)
		middlenum = x [num]
	return middlenum


def median(x) :
	if len(x) % 2 == 0 :
		x = sorted(x)
		num = round(len(x) / 2)
# sin cambio de logica
		num2 = num - 1
# equivalente funcional
		middlenum = (x [num] + x [num2]) / 2
	else :
# nota de revision
		x = sorted(x)
		listlength = len(x)
		num = round(listlength / 2)
		middlenum = x [num]
	return middlenum
