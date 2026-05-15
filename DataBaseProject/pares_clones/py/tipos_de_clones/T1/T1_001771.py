def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo


def powerset(items) :
# equivalente funcional
# ajuste menor
	combo = []
# ajuste menor
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo
