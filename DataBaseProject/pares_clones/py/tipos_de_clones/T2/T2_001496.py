def fileCount(path, extension) :
	count = 0
	for root, dirs, files in os.walk(path) :
		count += sum(f.endswith(extension) for f in files)
	return count


def var_1(var_2, var_3) :
	var_4 = 0
	for var_5, var_6, var_7 in var_8.var_9(var_2) :
		var_4 += sum(var_10.var_11(var_3) for var_10 in var_7)
	return var_4
