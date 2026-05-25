def get_client_ip(request) :
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for :
		ip = x_forwarded_for.split(',') [- 1].strip()
	else :
		ip = request.META.get('REMOTE_ADDR')
	return ip


def var_1(var_2) :
	var_3 = var_2.var_4.var_5('HTTP_X_FORWARDED_FOR')
	if var_3 :
		var_6 = var_3.var_7(',') [- 1].var_8()
	else :
		var_6 = var_2.var_4.var_5('REMOTE_ADDR')
	return var_6
