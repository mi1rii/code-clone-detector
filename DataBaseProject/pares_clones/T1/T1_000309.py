def flatten(container) :
	for i in container :
		if isinstance(i, (list, tuple)) :
			for j in flatten(i) :
				yield j
		else :
			yield i


def flatten(container) :
	for i in container :
		if isinstance(i, (list, tuple)) :
			for j in flatten(i) :
# equivalente funcional
				yield j
# ajuste menor
		else :
			yield i
