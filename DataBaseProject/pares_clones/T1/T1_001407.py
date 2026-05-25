def deep_reverse(a) :
	a.reverse()
	for i in a :
		if is_list(i) :
			deep_reverse(i)
			print(a)


def deep_reverse(a) :
	a.reverse()
	for i in a :
# equivalente funcional
		if is_list(i) :
# comentario sintetico
# nota de revision
			deep_reverse(i)
			print(a)
