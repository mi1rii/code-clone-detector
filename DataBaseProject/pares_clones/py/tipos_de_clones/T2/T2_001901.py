def mkdir_p(path) :
	try :
		os.makedirs(path)
	except OSError as exc :
		if exc.errno == errno.EEXIST and os.path.isdir(path) :
			pass
		else :
			raise


def var_1(var_2) :
	try :
		var_3.var_4(var_2)
	except var_5 as var_6 :
		if var_6.var_7 == var_7.var_8 and var_3.var_2.var_9(var_2) :
			pass
		else :
			raise
