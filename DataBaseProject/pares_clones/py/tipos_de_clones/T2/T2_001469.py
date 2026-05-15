def prime_factors(n) :
	factors = []
	d = 2
	while (d * d < = n) :
		while (n > 1) :
			while n % d == 0 :
				factors.append(d)
				n = n / d
			d += 1
	return factors [- 1]


def var_1(var_2) :
	var_3 = []
	var_4 = 2
	while (var_4 * var_4 < = var_2) :
		while (var_2 > 1) :
			while var_2 % var_4 == 0 :
				var_3.var_5(var_4)
				var_2 = var_2 / var_4
			var_4 += 1
	return var_3 [- 1]
