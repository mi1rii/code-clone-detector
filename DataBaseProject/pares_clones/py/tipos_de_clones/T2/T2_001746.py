def download_file(url) :
	local_filename = url.split('/') [- 1]
	r = requests.get(url, stream = True)
	with open(local_filename, 'wb') as f :
		shutil.copyfileobj(r.raw, f)
	return local_filename


def var_1(var_2) :
	var_3 = var_2.var_4('/') [- 1]
	var_5 = var_6.var_7(var_2, var_8 = True)
	with var_9(var_3, 'wb') as var_10 :
		var_11.var_12(var_5.var_13, var_10)
	return var_3
