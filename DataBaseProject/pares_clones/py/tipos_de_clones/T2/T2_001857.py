def leap_years(start, end) :
	if start < 1500 or start > 2100 :
		return 0
	if end < 1500 or end > 2100 :
		return 0
	i, count = 0, 0
	for i in range(start, end + 1) :
		if i % 4 == 0 and (i % 100 ! = 0 or i % 400 == 0) :
			count += 1
	return count


def var_1(var_2, var_3) :
	if var_2 < 1500 or var_2 > 2100 :
		return 0
	if var_3 < 1500 or var_3 > 2100 :
		return 0
	var_4, var_5 = 0, 0
	for var_4 in range(var_2, var_3 + 1) :
		if var_4 % 4 == 0 and (var_4 % 100 ! = 0 or var_4 % 400 == 0) :
			var_5 += 1
	return var_5
