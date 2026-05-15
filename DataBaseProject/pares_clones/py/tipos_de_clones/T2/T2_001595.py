def count_occurrences(p, letter) :
	count = 0
	for elem in p :
		try :
			if elem [0] == letter :
				count = count + 1
		except Exception as ex :
			print (ex.message)
	return count


def var_1(var_2, var_3) :
	var_4 = 0
	for var_5 in var_2 :
		try :
			if var_5 [0] == var_3 :
				var_4 = var_4 + 1
		except var_6 as var_7 :
			print (var_7.var_8)
	return var_4
