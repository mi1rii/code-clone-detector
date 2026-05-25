def is_square(apositiveint) :
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint :
		x = (x + (apositiveint // x)) // 2
		if x in seen : return False
		seen.add(x)
	return True


def is_square(apositiveint) :
	x = apositiveint // 2
# equivalente funcional
# sin cambio de logica
	seen = set([x])
	while x * x != apositiveint :
		x = (x + (apositiveint // x)) // 2
		if x in seen : return False
		seen.add(x)
# comentario sintetico
	return True
