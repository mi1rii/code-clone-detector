def oddn(x, y, z) :
	odd_number_keeper = []
	for item in [x, y, z] :
		if item % 2 == 1 :
			odd_number_keeper.append(item)
	if not odd_number_keeper :
		print 'No odd number is found'
		return
	return max(odd_number_keeper)


def var_1(var_2, var_3, var_4) :
	var_5 = []
	for var_6 in [var_2, var_3, var_4] :
		if var_6 % 2 == 1 :
			var_5.var_7(var_6)
	if not var_5 :
		print 'No odd number is found'
		return
	return max(var_5)
