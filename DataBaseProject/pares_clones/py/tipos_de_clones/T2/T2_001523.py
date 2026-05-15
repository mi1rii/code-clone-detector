def primes(n) :
	primfac = []
	d = 2
	while d * d < = n :
		while (n % d) == 0 :
			primfac.append(d)
			n //= d
		d += 1
	if n > 1 :
		primfac.append(n)
	return primfac


def var_1(var_2) :
	var_3 = []
	var_4 = 2
	while var_4 * var_4 < = var_2 :
		while (var_2 % var_4) == 0 :
			var_3.var_5(var_4)
			var_2 //= var_4
		var_4 += 1
	if var_2 > 1 :
		var_3.var_5(var_2)
	return var_3
