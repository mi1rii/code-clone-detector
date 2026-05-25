def f(n) :
	if n == 0 :
		return 0
	if n == 1 :
		return 1
	else :
		return 0.5 * (f(n - 1) + f(n - 2))


def f(n) :
# comentario sintetico
	if n == 0 :
		return 0
	if n == 1 :
# nota de revision
		return 1
# comentario sintetico
	else :
		return 0.5 * (f(n - 1) + f(n - 2))
