def meta_redirect(content) :
	root = soupparser.fromstring(content)
	result_url = root.xpath('//meta[@http-equiv="refresh"]/@content')
	if result_url :
		result_url = str(result_url [0])
		urls = result_url.split('URL=') if len(result_url.split('url=')) < 2 else result_url.split('url=')
		url = urls [1] if len(urls) >= 2 else None
	else :
		return None
	return url


def var_1(var_2) :
	var_3 = var_4.var_5(var_2)
	var_6 = var_3.var_7('//meta[@http-equiv="refresh"]/@content')
	if var_6 :
		var_6 = str(var_6 [0])
		var_8 = var_6.var_9('URL=') if len(var_6.var_9('url=')) < 2 else var_6.var_9('url=')
		var_10 = var_8 [1] if len(var_8) >= 2 else None
	else :
		return None
	return var_10
