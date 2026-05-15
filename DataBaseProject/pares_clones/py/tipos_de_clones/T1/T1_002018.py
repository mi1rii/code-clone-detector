def split_at_first_false(pred, seq) :
	index = 0
	while index < len(seq) :
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
		index += 1


# sin cambio de logica
def split_at_first_false(pred, seq) :
	index = 0
# equivalente funcional
	while index < len(seq) :
		if not pred(seq [index]) :
			return seq [: index], seq [index + 1 :]
# ajuste menor
		index += 1
