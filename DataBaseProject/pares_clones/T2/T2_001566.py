def pay_with_coins(amount) :
	coins = [0 for i in range(len(currencies))]
	amount = int(amount * 100)
	values = [c * 100 for c in currencies]
	for currency in values :
		i = values.index(currency)
		coins [i] = 0
		while amount > = currency :
			amount -= currency
			coins [i] += 1
	return coins


def var_1(var_2) :
	var_3 = [0 for var_4 in range(len(var_5))]
	var_2 = int(var_2 * 100)
	var_6 = [var_7 * 100 for var_7 in var_5]
	for var_8 in var_6 :
		var_4 = var_6.var_9(var_8)
		var_3 [var_4] = 0
		while var_2 > = var_8 :
			var_2 -= var_8
			var_3 [var_4] += 1
	return var_3
