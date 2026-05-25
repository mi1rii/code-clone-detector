def some_function(eggs) :
	if eggs not in [1, 2, 3] :
		do_error()
		return
	if eggs == 1 :
		do_something_1()
	elif eggs == 2 :
		do_something_2()
	elif eggs == 3 :
		do_something_3()
	else :
		assert False
	do_something_4()
	do_something_5()
	do_something_6()


def var_1(var_2) :
	if var_2 not in [1, 2, 3] :
		var_3()
		return
	if var_2 == 1 :
		var_4()
	elif var_2 == 2 :
		var_5()
	elif var_2 == 3 :
		var_6()
	else :
		assert False
	var_7()
	var_8()
	var_9()
