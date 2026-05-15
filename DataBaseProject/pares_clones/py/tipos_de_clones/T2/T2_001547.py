def specialMultiplication(n) :
	to_process = []
	result = 1
	if n >= 2 :
		to_process.append(n)
		while to_process :
			n = to_process.pop()
			result *= n
			if n >= 3 :
				to_process.append(n - 1)
				if n >= 4 :
					to_process.append(n - 2)
	return result


def var_1(var_2) :
	var_3 = []
	var_4 = 1
	if var_2 >= 2 :
		var_3.var_5(var_2)
		while var_3 :
			var_2 = var_3.var_6()
			var_4 *= var_2
			if var_2 >= 3 :
				var_3.var_5(var_2 - 1)
				if var_2 >= 4 :
					var_3.var_5(var_2 - 2)
	return var_4
