def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo


def powerset(items) :
# sin cambio de logica
# equivalente funcional
	combo = []
# sin cambio de logica
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo
