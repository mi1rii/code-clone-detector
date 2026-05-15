def my_function(a) :
	a = iter(a)
	while True :
		yield 10 * next(a)
		yield next(a)
		yield "foo" + next(a)


def var_1(var_2) :
	var_2 = var_3(var_2)
	while True :
		yield 10 * var_4(var_2)
		yield var_4(var_2)
		yield "foo" + var_4(var_2)
