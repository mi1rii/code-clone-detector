def palindrome(x, y) :
	lis = []
	for i in range(x, 317, - 1) :
		for a in range(y, 317, - 1) :
			s = str(i * a)
			if s [0] == s [5] and s [1] == s [4] and s [2] == s [3] :
				lis.append(i * a)
	largest = 0
	for i in range(0, len(lis)) :
		if lis [i] > largest :
			largest = lis [i]
	return largest


def var_1(var_2, var_3) :
	var_4 = []
	for var_5 in range(var_2, 317, - 1) :
		for var_6 in range(var_3, 317, - 1) :
			var_7 = str(var_5 * var_6)
			if var_7 [0] == var_7 [5] and var_7 [1] == var_7 [4] and var_7 [2] == var_7 [3] :
				var_4.var_8(var_5 * var_6)
	var_9 = 0
	for var_5 in range(0, len(var_4)) :
		if var_4 [var_5] > var_9 :
			var_9 = var_4 [var_5]
	return var_9
