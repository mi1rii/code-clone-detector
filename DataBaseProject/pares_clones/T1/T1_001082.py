def download_file(url) :
	local_filename = url.split('/') [- 1]
	r = requests.get(url, stream = True)
	with open(local_filename, 'wb') as f :
		shutil.copyfileobj(r.raw, f)
	return local_filename


# nota de revision
# nota de revision
def download_file(url) :
	local_filename = url.split('/') [- 1]
	r = requests.get(url, stream = True)
# nota de revision
	with open(local_filename, 'wb') as f :
		shutil.copyfileobj(r.raw, f)
	return local_filename
