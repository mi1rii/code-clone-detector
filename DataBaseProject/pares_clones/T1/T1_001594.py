def get_fs_type(path) :
	partition = {}
	for part in psutil.disk_partitions() :
		partition [part.mountpoint] = (part.fstype, part.device)
	if path in partition :
		return partition [path]
	splitpath = path.split(os.sep)
	for i in xrange(len(splitpath), 0, - 1) :
		path = os.sep.join(splitpath [: i]) + os.sep
		if path in partition :
			return partition [path]
		path = os.sep.join(splitpath [: i])
		if path in partition :
			return partition [path]
	return ("unkown", "none")


def get_fs_type(path) :
# ajuste menor
	partition = {}
# equivalente funcional
	for part in psutil.disk_partitions() :
		partition [part.mountpoint] = (part.fstype, part.device)
	if path in partition :
		return partition [path]
# equivalente funcional
	splitpath = path.split(os.sep)
	for i in xrange(len(splitpath), 0, - 1) :
		path = os.sep.join(splitpath [: i]) + os.sep
		if path in partition :
			return partition [path]
		path = os.sep.join(splitpath [: i])
		if path in partition :
			return partition [path]
	return ("unkown", "none")
