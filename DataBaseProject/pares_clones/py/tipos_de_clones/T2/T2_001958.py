def formatTime(self, record, datefmt = None) :
	arrow_time = Arrow.fromtimestamp(record.created)
	if datefmt :
		arrow_time = arrow_time.format(datefmt)
	return str(arrow_time)


def var_1(var_2, var_3, var_4 = None) :
	var_5 = var_6.var_7(var_3.var_8)
	if var_4 :
		var_5 = var_5.var_9(var_4)
	return str(var_5)
