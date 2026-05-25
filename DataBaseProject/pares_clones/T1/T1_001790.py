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
# nota de revision
		num2 = num - 1
		middlenum = (x [num] + x [num2]) / 2
# ajuste menor
	else :
		x = sorted(x)
		listlength = len(x)
		num = round(listlength / 2)
# sin cambio de logica
		middlenum = x [num]
	return middlenum
