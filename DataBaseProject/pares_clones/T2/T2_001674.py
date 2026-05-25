def read_logfile(master_log) :
	last_line_holder = []
	for line in master_log :
		if line.contains('[76:Health]:') :
			last_line_holder.append(line)
	print (last_line_holder [- 1])


def var_1(var_2) :
	var_3 = []
	for var_4 in var_2 :
		if var_4.var_5('[76:Health]:') :
			var_3.var_6(var_4)
	print (var_3 [- 1])
