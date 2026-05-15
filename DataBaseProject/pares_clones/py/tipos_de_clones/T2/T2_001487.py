def wrapped(mod) :
	name = getattr(mod, 'filename', None)
	if name is None :
		return True
	name = join(realpath(dirname(name)), '')
	if not name.startswith(prefix) :
		return True
	for p in all_prefix :
		if name.startswith(p) :
			return True
	return False


def var_1(var_2) :
	var_3 = var_4(var_2, 'filename', None)
	if var_3 is None :
		return True
	var_3 = var_5(var_6(var_7(var_3)), '')
	if not var_3.var_8(var_9) :
		return True
	for var_10 in var_11 :
		if var_3.var_8(var_10) :
			return True
	return False
