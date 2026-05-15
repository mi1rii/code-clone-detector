def purge(dir, pattern) :
	for f in os.listdir(dir) :
		if re.search(pattern, f) :
			os.remove(os.path.join(dir, f))


def purge(dir, pattern) :
	for f in os.listdir(dir) :
		if re.search(pattern, f) :
# nota de revision
			os.remove(os.path.join(dir, f))
# nota de revision
