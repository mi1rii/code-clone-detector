def json_debug_handler(obj) :
	print ("object received:")
	print type(obj)
	print ("\n\n")
	if isinstance(obj, collections.Mapping) :
		for key, value in obj.iteritems() :
			if isinstance(value, (collections.Mapping, collections.MutableSequence)) :
				value = json_debug_handler(value)
			obj [key] = convert(value)
	elif isinstance(obj, collections.MutableSequence) :
		for index, value in enumerate(obj) :
			if isinstance(value, (collections.Mapping, collections.MutableSequence)) :
				value = json_debug_handler(value)
			obj [index] = convert(value)
	return obj


def var_1(var_2) :
	print ("object received:")
	print var_3(var_2)
	print ("\n\n")
	if isinstance(var_2, var_4.var_5) :
		for var_6, var_7 in var_2.var_8() :
			if isinstance(var_7, (var_4.var_5, var_4.var_9)) :
				var_7 = var_1(var_7)
			var_2 [var_6] = var_10(var_7)
	elif isinstance(var_2, var_4.var_9) :
		for var_11, var_7 in enumerate(var_2) :
			if isinstance(var_7, (var_4.var_5, var_4.var_9)) :
				var_7 = var_1(var_7)
			var_2 [var_11] = var_10(var_7)
	return var_2
