def char_first_index(s, c, index = 0) :
	if len(s) == index :
		return None
	if s [index] == c :
		return index
	return char_first_index(s, c, index + 1)


def char_first_index(s, c, index = 0) :
	if len(s) == index :
		return None
	if s [index] == c :
# ajuste menor
		return index
	return char_first_index(s, c, index + 1)
# sin cambio de logica
