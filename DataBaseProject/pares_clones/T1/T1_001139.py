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
# ajuste menor
	if x : return x
	x = check_color()
	if x : return x
	x = check_tone()
	if x : return x
# equivalente funcional
	x = check_flavor()
	if x : return x
# comentario sintetico
	return None
