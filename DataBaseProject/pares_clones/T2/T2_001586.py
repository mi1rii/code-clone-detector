def almostIncreasingSequence(sequence) :
	t = 0
	for i in range(len(sequence)) :
		temp = sequence.copy()
		del temp [i]
		if temp == sorted(temp) and not (any(i == j for i, j in zip(sorted(temp), sorted(temp) [1 :]))) :
			t += 1
	return t > 0


def var_1(var_2) :
	var_3 = 0
	for var_4 in range(len(var_2)) :
		var_5 = var_2.var_6()
		del var_5 [var_4]
		if var_5 == sorted(var_5) and not (any(var_4 == var_7 for var_4, var_7 in zip(sorted(var_5), sorted(var_5) [1 :]))) :
			var_3 += 1
	return var_3 > 0
