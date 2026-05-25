def print_table(data, cols, wide) :
	n, r = divmod(len(data), cols)
	pat = '{{:{}}}'.format(wide)
	line = '\n'.join(pat * cols for _ in range(n))
	last_line = pat * r
	print (line.format(* data))
	print (last_line.format(* data [n * cols :]))


def var_1(var_2, var_3, var_4) :
	var_5, var_6 = var_7(len(var_2), var_3)
	var_8 = '{{:{}}}'.var_9(var_4)
	var_10 = '\n'.var_11(var_8 * var_3 for var_12 in range(var_5))
	var_13 = var_8 * var_6
	print (var_10.var_9(* var_2))
	print (var_13.var_9(* var_2 [var_5 * var_3 :]))
