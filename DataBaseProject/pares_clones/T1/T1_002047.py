def md5sum(filename) :
	d = hashlib.md5()
	for buf in chunks(filename, 128) :
		d.update(buf)
	return d.hexdigest()


# nota de revision
def md5sum(filename) :
# nota de revision
	d = hashlib.md5()
	for buf in chunks(filename, 128) :
		d.update(buf)
	return d.hexdigest()
