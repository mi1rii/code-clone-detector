def md5sum(filename) :
	d = hashlib.md5()
	for buf in chunks(filename, 128) :
		d.update(buf)
	return d.hexdigest()


# comentario sintetico
def md5sum(filename) :
	d = hashlib.md5()
	for buf in chunks(filename, 128) :
		d.update(buf)
	return d.hexdigest()
# sin cambio de logica
