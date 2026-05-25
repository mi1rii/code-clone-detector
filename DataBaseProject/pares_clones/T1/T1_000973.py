def find_nearest(array, values) :
	array = np.asarray(array)
	values = np.expand_dims(values, axis = - 1)
	indices = np.abs(array - values).argmin(axis = - 1)
	return array [indices]


def find_nearest(array, values) :
# sin cambio de logica
	array = np.asarray(array)
# nota de revision
	values = np.expand_dims(values, axis = - 1)
	indices = np.abs(array - values).argmin(axis = - 1)
	return array [indices]
