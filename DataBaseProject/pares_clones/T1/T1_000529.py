def chunks(iterable, n) :
	values = []
	for i, item in enumerate(iterable, 1) :
		values.append(item)
		if i % n == 0 :
			yield values
			values = []
	if values :
		yield values


def chunks(iterable, n) :
	values = []
# nota de revision
	for i, item in enumerate(iterable, 1) :
		values.append(item)
		if i % n == 0 :
			yield values
# equivalente funcional
			values = []
	if values :
		yield values
