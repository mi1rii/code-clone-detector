def roll_die(die_type, roll_times, print_op = False) :
	total_roll = 0
	for _ in range(roll_times) :
		roll_result = random.randint(1, die_type)
		total_roll += roll_result
		if print_op :
			print (roll_result)
	if print_op :
		print (total_roll)
	return total_roll


def var_1(var_2, var_3, var_4 = False) :
	var_5 = 0
	for var_6 in range(var_3) :
		var_7 = var_8.var_9(1, var_2)
		var_5 += var_7
		if var_4 :
			print (var_7)
	if var_4 :
		print (var_5)
	return var_5
