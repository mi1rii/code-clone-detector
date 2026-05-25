def myfun(my_list, n, par1 = '') :
	new_list = ([my_fun2(i, j) for j in range(n)] for i in range(n))
	if par1 ! = '' :
		new_list = filter(eq(par1), new_list)
	return list(new_list)


def var_1(var_2, var_3, var_4 = '') :
	var_5 = ([var_6(var_7, var_8) for var_8 in range(var_3)] for var_7 in range(var_3))
	if var_4 ! = '' :
		var_5 = filter(var_9(var_4), var_5)
	return list(var_5)
