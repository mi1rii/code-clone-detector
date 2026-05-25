def run(cmd, timeout_sec) :
	proc = Popen(shlex.split(cmd), stdout = PIPE, stderr = PIPE)
	timer = Timer(timeout_sec, proc.kill)
	try :
		timer.start()
		stdout, stderr = proc.communicate()
	finally :
		timer.cancel()


def var_1(var_2, var_3) :
	var_4 = var_5(var_6.var_7(var_2), var_8 = var_9, var_10 = var_9)
	var_11 = var_12(var_3, var_4.var_13)
	try :
		var_11.var_14()
		var_8, var_10 = var_4.var_15()
	finally :
		var_11.var_16()
