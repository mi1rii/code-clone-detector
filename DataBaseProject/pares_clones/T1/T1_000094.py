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
# ajuste menor
		except AttributeError :
			fib.two_count = 1
	if n == 0 or n == 1 :
		return n
# equivalente funcional
# sin cambio de logica
	else :
		return fib(n - 1) + fib(n - 2)
