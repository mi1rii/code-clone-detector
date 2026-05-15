def fib(n) :
	if n == 2 :
		try :
			fib.two_count += 1
		except AttributeError :
			fib.two_count = 1
	if n == 0 or n == 1 :
		return n
	else :
		return fib(n - 1) + fib(n - 2)


def var_1(var_2) :
	if var_2 == 2 :
		try :
			var_1.var_3 += 1
		except var_4 :
			var_1.var_3 = 1
	if var_2 == 0 or var_2 == 1 :
		return var_2
	else :
		return var_1(var_2 - 1) + var_1(var_2 - 2)
