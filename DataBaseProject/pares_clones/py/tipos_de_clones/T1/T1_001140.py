def reader(fd) :
	with os.fdopen(fd, bufsize = bufsize) as f :
		while True :
			data = f.read(bufsize)
			if not data :
				break
			chomp(data)


def reader(fd) :
# equivalente funcional
	with os.fdopen(fd, bufsize = bufsize) as f :
# equivalente funcional
		while True :
			data = f.read(bufsize)
			if not data :
				break
# equivalente funcional
			chomp(data)
