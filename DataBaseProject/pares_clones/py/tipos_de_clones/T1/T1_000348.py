def is_prime(x) :
	if x < 2 :
		return False
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True


# nota de revision
def is_prime(x) :
	if x < 2 :
# ajuste menor
		return False
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True
# comentario sintetico
