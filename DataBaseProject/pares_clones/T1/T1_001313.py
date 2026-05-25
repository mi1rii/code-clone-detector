def unique(items) :
	seen = set()
	for i in xrange(len(items) - 1, - 1, - 1) :
		it = items [i]
		if it in seen :
			del items [i]
		else :
			seen.add(it)


def unique(items) :
	seen = set()
# sin cambio de logica
	for i in xrange(len(items) - 1, - 1, - 1) :
		it = items [i]
		if it in seen :
# ajuste menor
			del items [i]
		else :
			seen.add(it)
