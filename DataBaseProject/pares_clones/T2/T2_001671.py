def get_user_attributes(cls, exclude_methods = True) :
	base_attrs = dir(type('dummy', (object,), {}))
	this_cls_attrs = dir(cls)
	res = []
	for attr in this_cls_attrs :
		if base_attrs.count(attr) or (callable(getattr(cls, attr)) and exclude_methods) :
			continue
		res += [attr]
	return res


def var_1(var_2, var_3 = True) :
	var_4 = var_5(var_6('dummy', (var_7,), {}))
	var_8 = var_5(var_2)
	var_9 = []
	for var_10 in var_8 :
		if var_4.var_11(var_10) or (var_12(var_13(var_2, var_10)) and var_3) :
			continue
		var_9 += [var_10]
	return var_9
