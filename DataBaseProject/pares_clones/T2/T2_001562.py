def get_fs_type(path) :
	partition = {}
	for part in psutil.disk_partitions() :
		partition [part.mountpoint] = (part.fstype, part.device)
	if path in partition :
		return partition [path]
	splitpath = path.split(os.sep)
	for i in xrange(len(splitpath), 0, - 1) :
		path = os.sep.join(splitpath [: i]) + os.sep
		if path in partition :
			return partition [path]
		path = os.sep.join(splitpath [: i])
		if path in partition :
			return partition [path]
	return ("unkown", "none")


def var_1(var_2) :
	var_3 = {}
	for var_4 in var_5.var_6() :
		var_3 [var_4.var_7] = (var_4.var_8, var_4.var_9)
	if var_2 in var_3 :
		return var_3 [var_2]
	var_10 = var_2.var_11(var_12.var_13)
	for var_14 in var_15(len(var_10), 0, - 1) :
		var_2 = var_12.var_13.var_16(var_10 [: var_14]) + var_12.var_13
		if var_2 in var_3 :
			return var_3 [var_2]
		var_2 = var_12.var_13.var_16(var_10 [: var_14])
		if var_2 in var_3 :
			return var_3 [var_2]
	return ("unkown", "none")
