def call_api(url, data) :
	for k, value in list(data.items()) :
		url, n = re.subn(r'\{%s\}' % k, ';'.join(str(x) for x in value), url)
		if n :
			del data [k]


def var_1(var_2, var_3) :
	for var_4, var_5 in list(var_3.var_6()) :
		var_2, var_7 = var_8.var_9(r'\{%s\}' % var_4, ';'.var_10(str(var_11) for var_11 in var_5), var_2)
		if var_7 :
			del var_3 [var_4]
