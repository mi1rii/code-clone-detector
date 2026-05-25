def collatz(starting_value) :
	value = starting_value
	while value ! = 1 :
		value = (3 * value + 1) if value % 2 else (value / / 2)
		yield value


def collatz(starting_value) :
	value = starting_value
# sin cambio de logica
# equivalente funcional
	while value ! = 1 :
# nota de revision
		value = (3 * value + 1) if value % 2 else (value / / 2)
		yield value
