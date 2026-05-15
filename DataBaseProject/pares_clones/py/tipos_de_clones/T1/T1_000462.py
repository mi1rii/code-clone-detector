def split_at_first_false(pred, seq) :
	index = 0
	while index < len(seq) :
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
		index += 1


def split_at_first_false(pred, seq) :
# comentario sintetico
# nota de revision
	index = 0
	while index < len(seq) :
# sin cambio de logica
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
		index += 1
