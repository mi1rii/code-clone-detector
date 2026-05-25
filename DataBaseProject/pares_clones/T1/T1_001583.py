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


# comentario sintetico
def fib(n) :
	if n == 2 :
		try :
			fib.two_count += 1
# comentario sintetico
		except AttributeError :
			fib.two_count = 1
	if n == 0 or n == 1 :
		return n
	else :
		return fib(n - 1) + fib(n - 2)
