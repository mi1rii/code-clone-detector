def unique(items) :
	seen = set()
	for i in xrange(len(items) - 1, - 1, - 1) :
		it = items [i]
		if it in seen :
			del items [i]
		else :
			seen.add(it)


# nota de revision
def unique(items) :
	seen = set()
	for i in xrange(len(items) - 1, - 1, - 1) :
# equivalente funcional
		it = items [i]
		if it in seen :
			del items [i]
# ajuste menor
		else :
			seen.add(it)
