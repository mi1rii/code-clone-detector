def spiral(width, height) :
	if width < 1 or height < 1 :
		raise ValueError
	x, y = width / / 2, height / / 2
	dx, dy = NORTH
	matrix = [[None] * width for _ in range(height)]
	count = 0
	while True :
		count += 1
		matrix [y] [x] = count
		new_dx, new_dy = turn_right [dx, dy]
		new_x, new_y = x + new_dx, y + new_dy
		if (0 < = new_x < width and 0 < = new_y < height and
		matrix [new_y] [new_x] is None) :
			x, y = new_x, new_y
			dx, dy = new_dx, new_dy
		else :
			x, y = x + dx, y + dy
			if not (0 < = x < width and 0 < = y < height) :
				return matrix


def var_1(var_2, var_3) :
	if var_2 < 1 or var_3 < 1 :
		raise var_4
	var_5, var_6 = var_2 / / 2, var_3 / / 2
	var_7, var_8 = var_9
	var_10 = [[None] * var_2 for var_11 in range(var_3)]
	var_12 = 0
	while True :
		var_12 += 1
		var_10 [var_6] [var_5] = var_12
		var_13, var_14 = var_15 [var_7, var_8]
		var_16, var_17 = var_5 + var_13, var_6 + var_14
		if (0 < = var_16 < var_2 and 0 < = var_17 < var_3 and
		var_10 [var_17] [var_16] is None) :
			var_5, var_6 = var_16, var_17
			var_7, var_8 = var_13, var_14
		else :
			var_5, var_6 = var_5 + var_7, var_6 + var_8
			if not (0 < = var_5 < var_2 and 0 < = var_6 < var_3) :
				return var_10
