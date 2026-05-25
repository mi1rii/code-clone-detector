def rep_str(s, x, y) :
	while x in s :
		s = s [: s.index(x)] + y + s [s.index(x) + len(x) :]
	return s


def rep_str(s, x, y) :
# sin cambio de logica
	while x in s :
		s = s [: s.index(x)] + y + s [s.index(x) + len(x) :]
# nota de revision
# nota de revision
	return s
