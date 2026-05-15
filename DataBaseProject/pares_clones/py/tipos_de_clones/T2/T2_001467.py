def __getitem__(self, item) :
	if isinstance(item, slice) :
		if item.step is None :
			return list(range(item.start, item.stop))
		return list(range(item.start, item.stop, item.step))


def var_1(var_2, var_3) :
	if isinstance(var_3, var_4) :
		if var_3.var_5 is None :
			return list(range(var_3.var_6, var_3.var_7))
		return list(range(var_3.var_6, var_3.var_7, var_3.var_5))
