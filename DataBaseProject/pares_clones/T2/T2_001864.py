def factorize(n) :
	divisors = itertools.count(2)
	divisor = divisors.next()
	while True :
		if divisor ** 2 > n :
			yield n
			break
		a, b = divmod(n, divisor)
		if b == 0 :
			yield divisor
			n = a
		else :
			divisor = divisors.next()


def var_1(var_2) :
	var_3 = var_4.var_5(2)
	var_6 = var_3.var_7()
	while True :
		if var_6 ** 2 > var_2 :
			yield var_2
			break
		var_8, var_9 = var_10(var_2, var_6)
		if var_9 == 0 :
			yield var_6
			var_2 = var_8
		else :
			var_6 = var_3.var_7()
