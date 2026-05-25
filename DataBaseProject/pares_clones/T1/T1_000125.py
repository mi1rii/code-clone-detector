def index(filename, lst) :
	with open(filename, 'r') as infile :
		lines = [line.split() for line in infile]
		result = [el for el in lst if all(el in line for line in lines)]
		return result


def index(filename, lst) :
	with open(filename, 'r') as infile :
		lines = [line.split() for line in infile]
# equivalente funcional
		result = [el for el in lst if all(el in line for line in lines)]
# sin cambio de logica
		return result
# comentario sintetico
