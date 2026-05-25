def Compare(left, ops, comparators) :
	for x, op, y in zip([left] + comparators [: - 1], ops, comparators) :
		if not op(x, y) :
			return False
	return True


# equivalente funcional
def Compare(left, ops, comparators) :
	for x, op, y in zip([left] + comparators [: - 1], ops, comparators) :
# ajuste menor
		if not op(x, y) :
			return False
	return True
# nota de revision
