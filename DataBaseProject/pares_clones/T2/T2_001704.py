def productFib(prod) :
	power = math.log(prod * 5) / log_phi
	i = int(round(power - 1, 7) / 2) + 1
	low = f(i)
	high = f(i + 1)
	answer = [low, high, low * high == prod]
	return answer


def var_1(var_2) :
	var_3 = var_4.var_5(var_2 * 5) / var_6
	var_7 = int(var_8(var_3 - 1, 7) / 2) + 1
	var_9 = var_10(var_7)
	var_11 = var_10(var_7 + 1)
	var_12 = [var_9, var_11, var_9 * var_11 == var_2]
	return var_12
