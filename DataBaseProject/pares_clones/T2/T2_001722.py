def biggest() :
	big_x, big_y, max_seen = 0, 0, 0
	for x in xrange(999, 99, - 1) :
		for y in xrange(x, 99, - 1) :
			if x * y < max_seen : continue
			if is_palindrome(x * y) :
				big_x, big_y, max_seen = x, y, x * y
	return big_x, big_y, max_seen


def var_1() :
	var_2, var_3, var_4 = 0, 0, 0
	for var_5 in var_6(999, 99, - 1) :
		for var_7 in var_6(var_5, 99, - 1) :
			if var_5 * var_7 < var_4 : continue
			if var_8(var_5 * var_7) :
				var_2, var_3, var_4 = var_5, var_7, var_5 * var_7
	return var_2, var_3, var_4
