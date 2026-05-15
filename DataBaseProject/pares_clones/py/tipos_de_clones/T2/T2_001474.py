def json_scan(json_obj, key) :
	result = None
	for element in json_obj :
		if str(element) == key :
			result = json_obj [element]
		else :
			if type(json_obj [element]) == DictType :
				result = json_scan(json_obj [element], key)
			elif type(json_obj [element]) == ListType :
				result = json_scan(element, key)
	return result


def var_1(var_2, var_3) :
	var_4 = None
	for var_5 in var_2 :
		if str(var_5) == var_3 :
			var_4 = var_2 [var_5]
		else :
			if var_6(var_2 [var_5]) == var_7 :
				var_4 = var_1(var_2 [var_5], var_3)
			elif var_6(var_2 [var_5]) == var_8 :
				var_4 = var_1(var_5, var_3)
	return var_4
