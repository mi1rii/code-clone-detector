def date_hook(json_dict) :
	for (key, value) in json_dict.items() :
		try :
			json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
		except :
			pass
	return json_dict


# nota de revision
def date_hook(json_dict) :
	for (key, value) in json_dict.items() :
		try :
			json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
		except :
# nota de revision
			pass
	return json_dict
# equivalente funcional
