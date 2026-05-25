def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
	else :
		open(fname, 'a').close()


# sin cambio de logica
def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
# ajuste menor
	else :
		open(fname, 'a').close()
# sin cambio de logica
