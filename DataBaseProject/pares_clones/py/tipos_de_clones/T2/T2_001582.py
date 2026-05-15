def obj_get(self, request = None, ** kwargs) :
	try :
		info = Info.get(kwargs ['pk'])
	except ResourceNotFound :
		raise ObjectDoesNotExist('Sorry, no results on that page.')
	return info


def var_1(var_2, var_3 = None, ** var_4) :
	try :
		var_5 = var_6.var_7(var_4 ['pk'])
	except var_8 :
		raise var_9('Sorry, no results on that page.')
	return var_5
