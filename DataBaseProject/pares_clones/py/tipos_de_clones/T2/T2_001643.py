def ping(self, host) :
	res = False
	ping_param = "-n 1" if system_name().lower() == "windows" else "-c 1"
	resultado = os.popen("ping " + ping_param + " " + host).read()
	if "TTL=" in resultado :
		res = True
	return res


def var_1(var_2, var_3) :
	var_4 = False
	var_5 = "-n 1" if var_6().var_7() == "windows" else "-c 1"
	var_8 = var_9.var_10("ping " + var_5 + " " + var_3).var_11()
	if "TTL=" in var_8 :
		var_4 = True
	return var_4
