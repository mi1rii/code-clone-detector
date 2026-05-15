def merge(a, low, mid, high) :
	l = a [low : mid + 1]
	r = a [mid + 1 : high + 1]
	k = 0; i = 0; j = 0;
	c = [0 for i in range(low, high + 1)]
	while (i < len(l) and j < len(r)) :
		if (l [i] < = r [j]) :
			c [k] = (l [i])
			k += 1
			i += 1
		else :
			c [k] = (r [j])
			j += 1
			k += 1
	while (i < len(l)) :
		c [k] = (l [i])
		k += 1
		i += 1
	while (j < len(r)) :
		c [k] = (r [j])
		k += 1
		j += 1
	a [low : high + 1] = c


def var_1(var_2, var_3, var_4, var_5) :
	var_6 = var_2 [var_3 : var_4 + 1]
	var_7 = var_2 [var_4 + 1 : var_5 + 1]
	var_8 = 0; var_9 = 0; var_10 = 0;
	var_11 = [0 for var_9 in range(var_3, var_5 + 1)]
	while (var_9 < len(var_6) and var_10 < len(var_7)) :
		if (var_6 [var_9] < = var_7 [var_10]) :
			var_11 [var_8] = (var_6 [var_9])
			var_8 += 1
			var_9 += 1
		else :
			var_11 [var_8] = (var_7 [var_10])
			var_10 += 1
			var_8 += 1
	while (var_9 < len(var_6)) :
		var_11 [var_8] = (var_6 [var_9])
		var_8 += 1
		var_9 += 1
	while (var_10 < len(var_7)) :
		var_11 [var_8] = (var_7 [var_10])
		var_8 += 1
		var_10 += 1
	var_2 [var_3 : var_5 + 1] = var_11
