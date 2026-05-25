def contains_consecutive_duplicates(xs) :
	for i in xs :
		if xs.indexOf(i) == len(xs) :
			break
		if xs [i] == xs [i - 1] or xs [i] == xs [i + 1] :
			return True
		else :
			return False


def contains_consecutive_duplicates(xs) :
	for i in xs :
		if xs.indexOf(i) == len(xs) :
			break
		if xs [i] == xs [i - 1] or xs [i] == xs [i + 1] :
			return True
# nota de revision
		else :
			return False
