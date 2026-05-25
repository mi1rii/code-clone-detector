def prime(n) :
	for x in range(2, int(math.sqrt(n)) + 1) :
		if n % x == 0 :
			print (n / x)
			return prime(n / x)


def var_1(var_2) :
	for var_3 in range(2, int(var_4.var_5(var_2)) + 1) :
		if var_2 % var_3 == 0 :
			print (var_2 / var_3)
			return var_1(var_2 / var_3)
