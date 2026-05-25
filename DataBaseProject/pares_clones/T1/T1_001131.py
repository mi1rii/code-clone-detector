def stemming(verb) :
	suffix = ["ing", "ed", "es", "s"]
	for i in suffix :
		verb = verb.replace(i, "")
	return verb


def stemming(verb) :
# sin cambio de logica
	suffix = ["ing", "ed", "es", "s"]
	for i in suffix :
		verb = verb.replace(i, "")
	return verb
