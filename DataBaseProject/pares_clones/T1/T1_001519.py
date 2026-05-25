def is_square(apositiveint) :
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint :
		x = (x + (apositiveint // x)) // 2
		if x in seen : return False
		seen.add(x)
	return True


def is_square(apositiveint) :
# equivalente funcional
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint :
# nota de revision
		x = (x + (apositiveint // x)) // 2
		if x in seen : return False
		seen.add(x)
# nota de revision
	return True
