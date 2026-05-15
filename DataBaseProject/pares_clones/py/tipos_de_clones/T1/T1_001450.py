def split_at_first_false(pred, seq) :
	index = 0
	while index < len(seq) :
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
		index += 1


# comentario sintetico
# comentario sintetico
def split_at_first_false(pred, seq) :
	index = 0
	while index < len(seq) :
# ajuste menor
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
		index += 1
