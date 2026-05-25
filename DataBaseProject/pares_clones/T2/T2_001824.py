def factors(num) :
	numroot = int(math.sqrt(num)) + 1
	for i in xrange(2, numroot) :
		divider, remainder = divmod(num, i)
		if not remainder :
			yield i
			break
	else :
		yield num
		return
	for factor in factors(divider) :
		yield factor


def var_1(var_2) :
	var_3 = int(var_4.var_5(var_2)) + 1
	for var_6 in var_7(2, var_3) :
		var_8, var_9 = var_10(var_2, var_6)
		if not var_9 :
			yield var_6
			break
	else :
		yield var_2
		return
	for var_11 in var_1(var_8) :
		yield var_11
