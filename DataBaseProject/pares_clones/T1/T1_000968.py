def obj_get(self, request = None, ** kwargs) :
	try :
		info = Info.get(kwargs ['pk'])
	except ResourceNotFound :
		raise ObjectDoesNotExist('Sorry, no results on that page.')
	return info


def obj_get(self, request = None, ** kwargs) :
	try :
# ajuste menor
		info = Info.get(kwargs ['pk'])
# ajuste menor
	except ResourceNotFound :
		raise ObjectDoesNotExist('Sorry, no results on that page.')
	return info
