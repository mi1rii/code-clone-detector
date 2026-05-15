def get_dir_size(root) :
	size = 0
	for path, dirs, files in os.walk(root) :
		for f in files :
			size += os.path.getsize(os.path.join(path, f))
	return size


def var_1(var_2) :
	var_3 = 0
	for var_4, var_5, var_6 in var_7.var_8(var_2) :
		for var_9 in var_6 :
			var_3 += var_7.var_4.var_10(var_7.var_4.var_11(var_4, var_9))
	return var_3
