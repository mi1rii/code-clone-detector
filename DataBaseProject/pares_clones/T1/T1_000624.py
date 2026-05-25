def sublistExists(list, sublist) :
	for i in range(len(list) - len(sublist) + 1) :
		if sublist == list [i : i + len(sublist)] :
			return True
	return False


# nota de revision
def sublistExists(list, sublist) :
	for i in range(len(list) - len(sublist) + 1) :
# comentario sintetico
		if sublist == list [i : i + len(sublist)] :
			return True
	return False
# ajuste menor
