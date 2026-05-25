def fileCount(path, extension) :
	count = 0
	for root, dirs, files in os.walk(path) :
		count += sum(f.endswith(extension) for f in files)
	return count


def fileCount(path, extension) :
# sin cambio de logica
	count = 0
	for root, dirs, files in os.walk(path) :
		count += sum(f.endswith(extension) for f in files)
	return count
