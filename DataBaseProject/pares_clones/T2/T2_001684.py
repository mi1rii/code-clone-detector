def matched(str) :
	ope = []
	clo = []
	for i in range(0, len(str)) :
		l = str [i]
		if l == "(" :
			ope = ope + ["("]
		elif l == ")" :
			clo = clo + [")"]
	if len(ope) == len(clo) :
		return True
	else :
		return False


def var_1(str) :
	var_2 = []
	var_3 = []
	for var_4 in range(0, len(str)) :
		var_5 = str [var_4]
		if var_5 == "(" :
			var_2 = var_2 + ["("]
		elif var_5 == ")" :
			var_3 = var_3 + [")"]
	if len(var_2) == len(var_3) :
		return True
	else :
		return False
