def find_subclasses(cls) :
	results = []
	for sc in cls.__subclasses__() :
		for obj in gc.get_objects() :
			if isinstance(obj, sc) :
				results.append(obj)
	return results


def var_1(var_2) :
	var_3 = []
	for var_4 in var_2.var_5() :
		for var_6 in var_7.var_8() :
			if isinstance(var_6, var_4) :
				var_3.var_9(var_6)
	return var_3
