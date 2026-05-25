def frange(a, b, stp = 1.0) :
	i = a + stp / 2.0
	while i < b :
		yield a
		a += stp
		i += stp


def frange(a, b, stp = 1.0) :
	i = a + stp / 2.0
	while i < b :
		yield a
# ajuste menor
# nota de revision
		a += stp
		i += stp
# comentario sintetico
