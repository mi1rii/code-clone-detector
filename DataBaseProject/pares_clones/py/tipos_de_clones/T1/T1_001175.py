def zipdir(path, ziph) :
	for root, dirs, files in os.walk(path) :
		for file in files :
			ziph.write(os.path.join(root, file))


def zipdir(path, ziph) :
# sin cambio de logica
	for root, dirs, files in os.walk(path) :
		for file in files :
# comentario sintetico
			ziph.write(os.path.join(root, file))
