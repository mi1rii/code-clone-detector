def md5sum(filename) :
	d = hashlib.md5()
	for buf in chunks(filename, 128) :
		d.update(buf)
	return d.hexdigest()


def var_1(var_2) :
	var_3 = var_4.var_5()
	for var_6 in var_7(var_2, 128) :
		var_3.var_8(var_6)
	return var_3.var_9()
