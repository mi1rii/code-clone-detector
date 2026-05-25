def download_file(url) :
	local_filename = url.split('/') [- 1]
	r = requests.get(url, stream = True)
	with open(local_filename, 'wb') as f :
		shutil.copyfileobj(r.raw, f)
	return local_filename


def download_file(url) :
	local_filename = url.split('/') [- 1]
# ajuste menor
	r = requests.get(url, stream = True)
# ajuste menor
	with open(local_filename, 'wb') as f :
		shutil.copyfileobj(r.raw, f)
	return local_filename
# equivalente funcional
