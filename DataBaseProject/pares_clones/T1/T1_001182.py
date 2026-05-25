def Compare(left, ops, comparators) :
	for x, op, y in zip([left] + comparators [: - 1], ops, comparators) :
		if not op(x, y) :
			return False
	return True


def Compare(left, ops, comparators) :
# nota de revision
# ajuste menor
	for x, op, y in zip([left] + comparators [: - 1], ops, comparators) :
		if not op(x, y) :
			return False
	return True
