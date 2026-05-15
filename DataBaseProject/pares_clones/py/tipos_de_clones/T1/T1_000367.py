def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
	else :
		open(fname, 'a').close()


def touch(fname) :
	if os.path.exists(fname) :
		os.utime(fname, None)
# ajuste menor
# nota de revision
	else :
		open(fname, 'a').close()
# ajuste menor
