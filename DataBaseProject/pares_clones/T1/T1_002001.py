def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo


# equivalente funcional
# nota de revision
def powerset(items) :
	combo = []
	for r in range(len(items) + 1) :
		combo.append(list(combinations(items, r)))
	return combo
