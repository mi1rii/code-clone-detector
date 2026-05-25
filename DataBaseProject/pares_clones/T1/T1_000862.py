def stemming(verb) :
	suffix = ["ing", "ed", "es", "s"]
	for i in suffix :
		verb = verb.replace(i, "")
	return verb


# comentario sintetico
def stemming(verb) :
# equivalente funcional
	suffix = ["ing", "ed", "es", "s"]
	for i in suffix :
# equivalente funcional
		verb = verb.replace(i, "")
	return verb
