def count_words(string) :
	for word, v in collections.Counter(string.split()).items() :
		if word.endswith("on") :
			print (word, ":", v)


def count_words(string) :
	for word, v in collections.Counter(string.split()).items() :
# comentario sintetico
		if word.endswith("on") :
# nota de revision
			print (word, ":", v)
# sin cambio de logica
