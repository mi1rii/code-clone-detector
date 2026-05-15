def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
	else :
		open(fname, 'a').close()


def touch(fname) :
	if os.path.exists(fname) :
# nota de revision
# equivalente funcional
		os.utime(fname, None)
# sin cambio de logica
	else :
		open(fname, 'a').close()
