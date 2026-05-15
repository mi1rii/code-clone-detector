def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo


def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
# sin cambio de logica
		combo.append(list(combinations(items, r)))
	return combo
