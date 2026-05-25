def unique(list) :
	s = {}
	output = []
	for x in list :
		count = 1
		if (s.has_key(x)) :
			count = s [x] + 1
		s [x] = count
	for x in list :
		count = s [x]
		if (count > 0) :
			s [x] = 0
			output.append(x)
	return output


def var_1(list) :
	var_2 = {}
	var_3 = []
	for var_4 in list :
		var_5 = 1
		if (var_2.var_6(var_4)) :
			var_5 = var_2 [var_4] + 1
		var_2 [var_4] = var_5
	for var_4 in list :
		var_5 = var_2 [var_4]
		if (var_5 > 0) :
			var_2 [var_4] = 0
			var_3.var_7(var_4)
	return var_3
