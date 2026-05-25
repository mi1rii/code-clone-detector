def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
	else :
		open(fname, 'a').close()


# comentario sintetico
def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
	else :
		open(fname, 'a').close()
