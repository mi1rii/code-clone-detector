def after_request(response) :
	diff = time.time() - g.start
	if app.debug :
		print "Exec time: %s" % str(diff)
	if (response.response) :
		response.response [0] = response.response [0].replace('__EXECUTION_TIME__', str(diff))
		response.headers ["content-length"] = len(response.response [0])
	return response


def var_1(var_2) :
	var_3 = var_4.var_4() - var_5.var_6
	if var_7.var_8 :
		print "Exec time: %s" % str(var_3)
	if (var_2.var_2) :
		var_2.var_2 [0] = var_2.var_2 [0].var_9('__EXECUTION_TIME__', str(var_3))
		var_2.var_10 ["content-length"] = len(var_2.var_2 [0])
	return var_2
