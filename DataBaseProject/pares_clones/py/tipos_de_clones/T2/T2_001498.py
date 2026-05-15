def __getitem__(self, key) :
	if isinstance(key, int) :
		return super(MyOrderedDict, self).__getitem__(self.keys() [key])
	if isinstance(key, slice) :
		return [super(MyOrderedDict, self).__getitem__(k) for k in self.keys() [key]]
	return super(MyOrderedDict, self).__getitem__(key)


def var_1(var_2, var_3) :
	if isinstance(var_3, int) :
		return var_4(var_5, var_2).var_1(var_2.var_6() [var_3])
	if isinstance(var_3, var_7) :
		return [var_4(var_5, var_2).var_1(var_8) for var_8 in var_2.var_6() [var_3]]
	return var_4(var_5, var_2).var_1(var_3)
