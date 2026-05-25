def median(midlist) :
	midlist.sort()
	lens = len(midlist)
	if lens % 2 ! = 0 :
		midl = (lens / 2)
		res = midlist [midl]
	else :
		odd = (lens / 2) - 1
		ev = (lens / 2)
		res = float(midlist [odd] + midlist [ev]) / float(2)
	return res


def var_1(var_2) :
	var_2.var_3()
	var_4 = len(var_2)
	if var_4 % 2 ! = 0 :
		var_5 = (var_4 / 2)
		var_6 = var_2 [var_5]
	else :
		var_7 = (var_4 / 2) - 1
		var_8 = (var_4 / 2)
		var_6 = float(var_2 [var_7] + var_2 [var_8]) / float(2)
	return var_6
