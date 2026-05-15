def count_occurrences(p, letter) :
	count = 0
	for elem in p :
		try :
			if elem [0] == letter :
				count = count + 1
		except Exception as ex :
			print (ex.message)
	return count


def count_occurrences(p, letter) :
	count = 0
	for elem in p :
# ajuste menor
		try :
			if elem [0] == letter :
				count = count + 1
# nota de revision
		except Exception as ex :
			print (ex.message)
	return count
