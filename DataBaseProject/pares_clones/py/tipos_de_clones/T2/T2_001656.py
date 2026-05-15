def spiral(X, Y) :
	x = y = 0
	dx = 0
	dy = - 1
	for i in range(max(X, Y) ** 2) :
		if (- X / 2 < x < = X / 2) and (- Y / 2 < y < = Y / 2) :
			yield x, y
		if x == y or (x < 0 and x == - y) or (x > 0 and x == 1 - y) :
			dx, dy = - dy, dx
		x, y = x + dx, y + dy
	spiral_matrix_size = 5
	my_list = list(range(spiral_matrix_size ** 2))
	my_list = [my_list [x : x + spiral_matrix_size] for x in range(0, len(my_list), spiral_matrix_size)]
	print (my_list)
	for i, (x, y) in enumerate(spiral(spiral_matrix_size, spiral_matrix_size)) :
		diff = int(spiral_matrix_size / 2)
		my_list [x + diff] [y + diff] = i
	print (my_list)


def var_1(var_2, var_3) :
	var_4 = var_5 = 0
	var_6 = 0
	var_7 = - 1
	for var_8 in range(max(var_2, var_3) ** 2) :
		if (- var_2 / 2 < var_4 < = var_2 / 2) and (- var_3 / 2 < var_5 < = var_3 / 2) :
			yield var_4, var_5
		if var_4 == var_5 or (var_4 < 0 and var_4 == - var_5) or (var_4 > 0 and var_4 == 1 - var_5) :
			var_6, var_7 = - var_7, var_6
		var_4, var_5 = var_4 + var_6, var_5 + var_7
	var_9 = 5
	var_10 = list(range(var_9 ** 2))
	var_10 = [var_10 [var_4 : var_4 + var_9] for var_4 in range(0, len(var_10), var_9)]
	print (var_10)
	for var_8, (var_4, var_5) in enumerate(var_1(var_9, var_9)) :
		var_11 = int(var_9 / 2)
		var_10 [var_4 + var_11] [var_5 + var_11] = var_8
	print (var_10)
