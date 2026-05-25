def get_dir_size(root) :
	size = 0
	for path, dirs, files in os.walk(root) :
		for f in files :
			size += os.path.getsize(os.path.join(path, f))
	return size


def get_dir_size(root) :
# comentario sintetico
	size = 0
	for path, dirs, files in os.walk(root) :
		for f in files :
# ajuste menor
# sin cambio de logica
			size += os.path.getsize(os.path.join(path, f))
	return size
