def date_hook(json_dict) :
	for (key, value) in json_dict.items() :
		try :
			json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
		except :
			pass
	return json_dict


def var_1(var_2) :
	for (var_3, var_4) in var_2.var_5() :
		try :
			var_2 [var_3] = var_6.var_6.var_7(var_4, "%Y-%m-%dT%H:%M:%S")
		except :
			pass
	return var_2
