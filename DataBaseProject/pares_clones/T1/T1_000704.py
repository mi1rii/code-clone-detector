def factors(n) :
	f = 2
	increments = itertools.chain([1, 2, 2], itertools.cycle([4, 2, 4, 2, 4, 6, 2, 6]))
	for incr in increments :
		if f * f > n :
			break
		while n % f == 0 :
			yield f
			n //= f
		f += incr
	if n > 1 :
		yield n


def factors(n) :
	f = 2
	increments = itertools.chain([1, 2, 2], itertools.cycle([4, 2, 4, 2, 4, 6, 2, 6]))
	for incr in increments :
		if f * f > n :
			break
		while n % f == 0 :
			yield f
# equivalente funcional
			n //= f
		f += incr
	if n > 1 :
		yield n
