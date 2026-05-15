def execute(cmdArray, workingDir) :
	stdout = ''
	stderr = ''
	try :
		try :
			process = subprocess.Popen(cmdArray, cwd = workingDir, stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
		except OSError :
			return [False, '', 'ERROR : command(' + ' '.join(cmdArray) + ') could not get executed!']
		for line in iter(process.stdout.readline, b'') :
			try :
				echoLine = line.decode("utf-8")
			except :
				echoLine = str(line)
			stdout += echoLine
		for line in iter(process.stderr.readline, b'') :
			try :
				echoLine = line.decode("utf-8")
			except :
				echoLine = str(line)
			stderr += echoLine
	except (KeyboardInterrupt, SystemExit) as err :
		return [False, '', str(err)]
	process.stdout.close()
	returnCode = process.wait()
	if returnCode ! = 0 or stderr ! = '' :
		return [False, stdout, stderr]
	else :
		return [True, stdout, stderr]


def var_1(var_2, var_3) :
	var_4 = ''
	var_5 = ''
	try :
		try :
			var_6 = var_7.var_8(var_2, var_9 = var_3, var_4 = var_7.var_10, var_5 = var_7.var_10, var_11 = 1)
		except var_12 :
			return [False, '', 'ERROR : command(' + ' '.var_13(var_2) + ') could not get executed!']
		for var_14 in var_15(var_6.var_4.var_16, b'') :
			try :
				var_17 = var_14.var_18("utf-8")
			except :
				var_17 = str(var_14)
			var_4 += var_17
		for var_14 in var_15(var_6.var_5.var_16, b'') :
			try :
				var_17 = var_14.var_18("utf-8")
			except :
				var_17 = str(var_14)
			var_5 += var_17
	except (var_19, var_20) as var_21 :
		return [False, '', str(var_21)]
	var_6.var_4.var_22()
	var_23 = var_6.var_24()
	if var_23 ! = 0 or var_5 ! = '' :
		return [False, var_4, var_5]
	else :
		return [True, var_4, var_5]
