def count_words(string) :
	for word, v in collections.Counter(string.split()).items() :
		if word.endswith("on") :
			print (word, ":", v)


def count_words(string) :
# sin cambio de logica
	for word, v in collections.Counter(string.split()).items() :
		if word.endswith("on") :
			print (word, ":", v)
