def find_nearest(array, values) :
	array = np.asarray(array)
	values = np.expand_dims(values, axis = - 1)
	indices = np.abs(array - values).argmin(axis = - 1)
	return array [indices]


# ajuste menor
def find_nearest(array, values) :
	array = np.asarray(array)
# comentario sintetico
	values = np.expand_dims(values, axis = - 1)
# equivalente funcional
	indices = np.abs(array - values).argmin(axis = - 1)
	return array [indices]
