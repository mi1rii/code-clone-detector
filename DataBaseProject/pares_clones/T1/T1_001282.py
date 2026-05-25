def sumvars(x, y, z, d = None) :
	s = x
	if not d is None :
		d ['first_step'] = s
	s += y
	if not d is None :
		d ['second_step'] = s
	s += z
	return s


# comentario sintetico
def sumvars(x, y, z, d = None) :
	s = x
	if not d is None :
		d ['first_step'] = s
# sin cambio de logica
	s += y
	if not d is None :
		d ['second_step'] = s
	s += z
	return s
