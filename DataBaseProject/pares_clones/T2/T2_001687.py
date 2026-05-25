def choose(n, k) :
	if 0 < = k < = n :
		ntok = 1
		ktok = 1
		for t in xrange(1, min(k, n - k) + 1) :
			ntok *= n
			ktok *= t
			n -= 1
		return ntok / / ktok
	else :
		return 0


def var_1(var_2, var_3) :
	if 0 < = var_3 < = var_2 :
		var_4 = 1
		var_5 = 1
		for var_6 in var_7(1, min(var_3, var_2 - var_3) + 1) :
			var_4 *= var_2
			var_5 *= var_6
			var_2 -= 1
		return var_4 / / var_5
	else :
		return 0
