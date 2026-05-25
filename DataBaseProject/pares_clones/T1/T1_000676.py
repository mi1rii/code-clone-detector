def split_at_first_false(pred, seq) :
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]


# comentario sintetico
def split_at_first_false(pred, seq) :
# sin cambio de logica
# comentario sintetico
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]
