def chunks(iterable, n) :
	values = []
	for i, item in enumerate(iterable, 1) :
		values.append(item)
		if i % n == 0 :
			yield values
			values = []
	if values :
		yield values


# comentario sintetico
def chunks(iterable, n) :
	values = []
	for i, item in enumerate(iterable, 1) :
# sin cambio de logica
		values.append(item)
		if i % n == 0 :
			yield values
			values = []
	if values :
		yield values
