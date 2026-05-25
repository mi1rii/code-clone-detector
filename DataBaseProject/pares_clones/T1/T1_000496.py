def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo


def powerset(items) :
# nota de revision
# ajuste menor
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo
# equivalente funcional
