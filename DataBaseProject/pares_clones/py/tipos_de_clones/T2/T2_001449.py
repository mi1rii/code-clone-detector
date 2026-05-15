def get_data(self) :
	k = ''
	while True :
		c = timeout_call(sys.stdin.read, args = [1], timeout_duration = 0.05)
		if c is None :
			break
		k += c
	return k if k else False


def var_1(var_2) :
	var_3 = ''
	while True :
		var_4 = var_5(var_6.var_7.var_8, var_9 = [1], var_10 = 0.05)
		if var_4 is None :
			break
		var_3 += var_4
	return var_3 if var_3 else False
