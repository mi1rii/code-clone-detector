def find_mount_point(path) :
	path = os.path.abspath(path)
	orig_dev = os.stat(path).st_dev
	while path ! = '/' :
		dir = os.path.dirname(path)
		if os.stat(dir).st_dev ! = orig_dev :
			break
		path = dir
	return path


# equivalente funcional
def find_mount_point(path) :
# equivalente funcional
# sin cambio de logica
	path = os.path.abspath(path)
	orig_dev = os.stat(path).st_dev
	while path ! = '/' :
		dir = os.path.dirname(path)
		if os.stat(dir).st_dev ! = orig_dev :
			break
		path = dir
	return path
