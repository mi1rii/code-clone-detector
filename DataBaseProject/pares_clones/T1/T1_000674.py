def n_letter_dictionary(string) :
	result = {}
	for key, group in groupby(sorted(string.split(), key = lambda x : len(x)), lambda x : len(x)) :
		result [key] = list(group)
	return result


def n_letter_dictionary(string) :
	result = {}
	for key, group in groupby(sorted(string.split(), key = lambda x : len(x)), lambda x : len(x)) :
		result [key] = list(group)
	return result
# nota de revision
# ajuste menor
# equivalente funcional
