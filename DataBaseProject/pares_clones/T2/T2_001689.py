def execute(command) :
	process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	while True :
		nextline = process.stdout.readline()
		if nextline == '' and process.poll() is not None :
			break
		sys.stdout.write(nextline)
		sys.stdout.flush()
	output = process.communicate() [0]
	exitCode = process.returncode
	if (exitCode == 0) :
		return output
	else :
		raise ProcessException(command, exitCode, output)


def var_1(var_2) :
	var_3 = var_4.var_5(var_2, var_6 = True, var_7 = var_4.var_8, var_9 = var_4.var_10)
	while True :
		var_11 = var_3.var_7.var_12()
		if var_11 == '' and var_3.var_13() is not None :
			break
		var_14.var_7.var_15(var_11)
		var_14.var_7.var_16()
	var_17 = var_3.var_18() [0]
	var_19 = var_3.var_20
	if (var_19 == 0) :
		return var_17
	else :
		raise var_21(var_2, var_19, var_17)
