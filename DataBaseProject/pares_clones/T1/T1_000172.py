def flatten(container) :
	for i in container :
		if isinstance(i, (list, tuple)) :
			for j in flatten(i) :
				yield j
		else :
			yield i


# nota de revision
# sin cambio de logica
def flatten(container) :
	for i in container :
		if isinstance(i, (list, tuple)) :
			for j in flatten(i) :
				yield j
		else :
			yield i
