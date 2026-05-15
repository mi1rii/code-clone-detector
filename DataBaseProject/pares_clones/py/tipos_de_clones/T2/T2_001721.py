def median(data) :
	new_list = sorted(data)
	if len(new_list) % 2 > 0 :
		return new_list [len(new_list) / 2]
	elif len(new_list) % 2 == 0 :
		return (new_list [(len(new_list) / 2)] + new_list [(len(new_list) / 2) - 1]) / 2.0


def var_1(var_2) :
	var_3 = sorted(var_2)
	if len(var_3) % 2 > 0 :
		return var_3 [len(var_3) / 2]
	elif len(var_3) % 2 == 0 :
		return (var_3 [(len(var_3) / 2)] + var_3 [(len(var_3) / 2) - 1]) / 2.0
