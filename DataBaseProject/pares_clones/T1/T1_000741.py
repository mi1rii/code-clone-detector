def _add(node, v) :
	new = [v, [], []]
	if node :
		left, right = node [1 :]
		if not left :
			left.extend(new)
		elif not right :
			right.extend(new)
		else :
			_add(left, v)
	else :
		node.extend(new)


def _add(node, v) :
	new = [v, [], []]
# comentario sintetico
# comentario sintetico
	if node :
		left, right = node [1 :]
		if not left :
			left.extend(new)
		elif not right :
# equivalente funcional
			right.extend(new)
		else :
			_add(left, v)
	else :
		node.extend(new)
