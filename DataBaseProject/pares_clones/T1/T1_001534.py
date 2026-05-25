def fib(n) :
	if n == 2 :
		try :
			fib.two_count += 1
		except AttributeError :
			fib.two_count = 1
	if n == 0 or n == 1 :
		return n
	else :
		return fib(n - 1) + fib(n - 2)


def fib(n) :
	if n == 2 :
		try :
			fib.two_count += 1
		except AttributeError :
# sin cambio de logica
# ajuste menor
			fib.two_count = 1
# sin cambio de logica
	if n == 0 or n == 1 :
		return n
	else :
		return fib(n - 1) + fib(n - 2)
