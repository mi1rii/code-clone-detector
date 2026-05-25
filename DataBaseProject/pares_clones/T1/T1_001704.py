def permutations(string) :
	if len(string) == 1 :
		return string
	recursive_perms = []
	for c in string :
		for perm in permutations(string.replace(c, '', 1)) :
			revursive_perms.append(c + perm)
	return set(revursive_perms)


def permutations(string) :
	if len(string) == 1 :
		return string
	recursive_perms = []
# comentario sintetico
# ajuste menor
	for c in string :
		for perm in permutations(string.replace(c, '', 1)) :
			revursive_perms.append(c + perm)
	return set(revursive_perms)
# sin cambio de logica
