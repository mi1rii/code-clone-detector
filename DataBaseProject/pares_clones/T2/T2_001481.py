def get_size(start_path = '.') :
	total_size = 0
	seen = {}
	for dirpath, dirnames, filenames in os.walk(start_path) :
		for f in filenames :
			fp = os.path.join(dirpath, f)
			try :
				stat = os.stat(fp)
			except OSError :
				continue
			try :
				seen [stat.st_ino]
			except KeyError :
				seen [stat.st_ino] = True
			else :
				continue
			total_size += stat.st_size
	return total_size


def var_1(var_2 = '.') :
	var_3 = 0
	var_4 = {}
	for var_5, var_6, var_7 in var_8.var_9(var_2) :
		for var_10 in var_7 :
			var_11 = var_8.var_12.var_13(var_5, var_10)
			try :
				var_14 = var_8.var_14(var_11)
			except var_15 :
				continue
			try :
				var_4 [var_14.var_16]
			except var_17 :
				var_4 [var_14.var_16] = True
			else :
				continue
			var_3 += var_14.var_18
	return var_3
