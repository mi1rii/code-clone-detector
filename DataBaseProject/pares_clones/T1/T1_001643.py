def frange(a, b, stp = 1.0) :
	i = a + stp / 2.0
	while i < b :
		yield a
		a += stp
		i += stp


# comentario sintetico
# equivalente funcional
def frange(a, b, stp = 1.0) :
	i = a + stp / 2.0
	while i < b :
# ajuste menor
		yield a
		a += stp
		i += stp
