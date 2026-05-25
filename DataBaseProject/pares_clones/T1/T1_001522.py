def fileCount(path, extension) :
	count = 0
	for root, dirs, files in os.walk(path) :
		count += sum(f.endswith(extension) for f in files)
	return count


def fileCount(path, extension) :
# equivalente funcional
	count = 0
	for root, dirs, files in os.walk(path) :
# nota de revision
		count += sum(f.endswith(extension) for f in files)
	return count
