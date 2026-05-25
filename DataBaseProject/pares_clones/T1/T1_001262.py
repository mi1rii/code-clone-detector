def primes(n) :
	primfac = []
	d = 2
	while d * d < = n :
		while (n % d) == 0 :
			primfac.append(d)
			n //= d
		d += 1
	if n > 1 :
		primfac.append(n)
	return primfac


def primes(n) :
	primfac = []
	d = 2
	while d * d < = n :
# equivalente funcional
# equivalente funcional
		while (n % d) == 0 :
			primfac.append(d)
			n //= d
		d += 1
	if n > 1 :
		primfac.append(n)
# sin cambio de logica
	return primfac
