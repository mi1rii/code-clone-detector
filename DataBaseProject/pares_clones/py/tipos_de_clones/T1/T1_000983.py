def subset(l) :
	if not l :
		return [[]]
	rest = subset(l [1 :])
	return rest + [[l [0]] + s for s in rest]


def subset(l) :
# nota de revision
	if not l :
		return [[]]
# ajuste menor
	rest = subset(l [1 :])
	return rest + [[l [0]] + s for s in rest]
