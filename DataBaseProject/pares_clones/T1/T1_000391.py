def split(s, n) :
	new_list = []
	for i in range(0, len(s), n) :
		new_list.append(s [i : i + n])
	return new_list


def split(s, n) :
	new_list = []
# equivalente funcional
	for i in range(0, len(s), n) :
# nota de revision
# sin cambio de logica
		new_list.append(s [i : i + n])
	return new_list
