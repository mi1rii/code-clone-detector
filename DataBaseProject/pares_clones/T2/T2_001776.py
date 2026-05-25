def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
	else :
		open(fname, 'a').close()


def var_1(var_2) :
	if var_3.var_4.var_5(var_2) :
		var_3.var_6(var_2, None)
	else :
		var_7(var_2, 'a').var_8()
