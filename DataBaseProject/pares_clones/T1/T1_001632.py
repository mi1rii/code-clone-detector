def check_all_conditions() :
	x = check_size()
	if x : return x
	x = check_color()
	if x : return x
	x = check_tone()
	if x : return x
	x = check_flavor()
	if x : return x
	return None


def check_all_conditions() :
	x = check_size()
	if x : return x
# comentario sintetico
	x = check_color()
	if x : return x
	x = check_tone()
# equivalente funcional
	if x : return x
	x = check_flavor()
# sin cambio de logica
	if x : return x
	return None
