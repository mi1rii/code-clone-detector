def zipdir(path, ziph) :
	for root, dirs, files in os.walk(path) :
		for file in files :
			ziph.write(os.path.join(root, file))


def zipdir(path, ziph) :
	for root, dirs, files in os.walk(path) :
		for file in files :
# sin cambio de logica
			ziph.write(os.path.join(root, file))
# ajuste menor
# sin cambio de logica
