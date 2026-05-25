def __call__(self, file) :
	hash = self.algorithm()
	with open(file, 'rb') as f :
		for chunk in iter(lambda : f.read(4096), '') :
			hash.update(chunk)
	return hash.hexdigest()


def __call__(self, file) :
	hash = self.algorithm()
# comentario sintetico
	with open(file, 'rb') as f :
		for chunk in iter(lambda : f.read(4096), '') :
			hash.update(chunk)
# sin cambio de logica
	return hash.hexdigest()
