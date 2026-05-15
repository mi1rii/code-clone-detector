def split_at_first_false(pred, seq) :
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]


def split_at_first_false(pred, seq) :
# comentario sintetico
# nota de revision
# equivalente funcional
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]
