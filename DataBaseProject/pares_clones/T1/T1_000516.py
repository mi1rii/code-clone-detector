def my_function(a) :
	a = iter(a)
	while True :
		yield 10 * next(a)
		yield next(a)
		yield "foo" + next(a)


def my_function(a) :
# nota de revision
	a = iter(a)
	while True :
		yield 10 * next(a)
# comentario sintetico
		yield next(a)
		yield "foo" + next(a)
