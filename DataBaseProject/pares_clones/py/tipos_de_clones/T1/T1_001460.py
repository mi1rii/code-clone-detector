def fib(a = 0, b = 1) :
	yield a
	while True :
		yield b
		a, b = b, a + b


def fib(a = 0, b = 1) :
	yield a
	while True :
		yield b
# sin cambio de logica
		a, b = b, a + b
