def get_cost(x) :
	t_zone = 720
	max_rate = 5.5
	rate = 0.0208
	duration = x ['t1']
	if duration < t_zone :
		if (duration * rate) > = max_rate :
			return max_rate
		else :
			return (duration * rate)
	else :
		if duration > = 720 :
			x = int(duration / 720)
			y = ((duration % 720) * rate)
			if y > = max_rate :
				return ((x * max_rate) + max_rate)
			else :
				return ((x * max_rate) + y)


def var_1(var_2) :
	var_3 = 720
	var_4 = 5.5
	var_5 = 0.0208
	var_6 = var_2 ['t1']
	if var_6 < var_3 :
		if (var_6 * var_5) > = var_4 :
			return var_4
		else :
			return (var_6 * var_5)
	else :
		if var_6 > = 720 :
			var_2 = int(var_6 / 720)
			var_7 = ((var_6 % 720) * var_5)
			if var_7 > = var_4 :
				return ((var_2 * var_4) + var_4)
			else :
				return ((var_2 * var_4) + var_7)
