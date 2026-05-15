def countWords(s) :
	d = {}
	for word in s.split() :
		try :
			d [word] += 1
		except KeyError :
			d [word] = 1
	return d


def var_1(var_2) :
	var_3 = {}
	for var_4 in var_2.var_5() :
		try :
			var_3 [var_4] += 1
		except var_6 :
			var_3 [var_4] = 1
	return var_3
