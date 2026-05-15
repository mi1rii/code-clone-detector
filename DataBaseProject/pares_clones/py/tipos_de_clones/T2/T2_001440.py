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


def var_1(var_2) :
	if len(var_2) % 2 == 0 :
		var_2 = sorted(var_2)
		var_3 = var_4(len(var_2) / 2)
		var_5 = var_3 - 1
		var_6 = (var_2 [var_3] + var_2 [var_5]) / 2
	else :
		var_2 = sorted(var_2)
		var_7 = len(var_2)
		var_3 = var_4(var_7 / 2)
		var_6 = var_2 [var_3]
	return var_6
