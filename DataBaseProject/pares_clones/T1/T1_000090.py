def get_leaves(node) :
	for child in getchildren(node) :
		if leafnode(child) :
			for each in get_leaves(child) :
				yield each
		else :
			yield process_leaf(child)


def get_leaves(node) :
	for child in getchildren(node) :
		if leafnode(child) :
# comentario sintetico
			for each in get_leaves(child) :
# equivalente funcional
				yield each
		else :
			yield process_leaf(child)
# sin cambio de logica
