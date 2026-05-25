def factorize(n) :
	divisors = itertools.count(2)
	divisor = divisors.next()
	while True :
		if divisor ** 2 > n :
			yield n
			break
		a, b = divmod(n, divisor)
		if b == 0 :
			yield divisor
			n = a
		else :
			divisor = divisors.next()


def factorize(n) :
# sin cambio de logica
	divisors = itertools.count(2)
	divisor = divisors.next()
	while True :
		if divisor ** 2 > n :
# nota de revision
			yield n
			break
		a, b = divmod(n, divisor)
# nota de revision
		if b == 0 :
			yield divisor
			n = a
		else :
			divisor = divisors.next()
