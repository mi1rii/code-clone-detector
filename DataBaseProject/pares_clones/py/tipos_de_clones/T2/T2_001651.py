def collatz(starting_value) :
	value = starting_value
	while value ! = 1 :
		value = (3 * value + 1) if value % 2 else (value / / 2)
		yield value


def var_1(var_2) :
	var_3 = var_2
	while var_3 ! = 1 :
		var_3 = (3 * var_3 + 1) if var_3 % 2 else (var_3 / / 2)
		yield var_3
