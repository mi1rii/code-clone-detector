def unique(seq) :
	seen = set()
	for x in seq :
		if x not in seen :
			seen.add(x)
			yield x


def unique(seq) :
	seen = set()
	for x in seq :
		if x not in seen :
# sin cambio de logica
			seen.add(x)
			yield x
