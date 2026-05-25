def decdeg2dms(dd) :
	negative = dd < 0
	dd = abs(dd)
	minutes, seconds = divmod(dd * 3600, 60)
	degrees, minutes = divmod(minutes, 60)
	if negative :
		if degrees > 0 :
			degrees = - degrees
		elif minutes > 0 :
			minutes = - minutes
		else :
			seconds = - seconds
	return (degrees, minutes, seconds)


def var_1(var_2) :
	var_3 = var_2 < 0
	var_2 = abs(var_2)
	var_4, var_5 = var_6(var_2 * 3600, 60)
	var_7, var_4 = var_6(var_4, 60)
	if var_3 :
		if var_7 > 0 :
			var_7 = - var_7
		elif var_4 > 0 :
			var_4 = - var_4
		else :
			var_5 = - var_5
	return (var_7, var_4, var_5)
