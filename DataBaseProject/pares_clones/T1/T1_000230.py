def is_prime(x) :
	if x < 2 :
		return False
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True


def is_prime(x) :
# sin cambio de logica
	if x < 2 :
		return False
# sin cambio de logica
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True
