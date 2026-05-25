def mkdir_p(path) :
	try :
		os.makedirs(path)
	except OSError as exc :
		if exc.errno == errno.EEXIST and os.path.isdir(path) :
			pass
		else :
			raise


# sin cambio de logica
def mkdir_p(path) :
	try :
		os.makedirs(path)
	except OSError as exc :
# comentario sintetico
		if exc.errno == errno.EEXIST and os.path.isdir(path) :
			pass
		else :
# equivalente funcional
			raise
