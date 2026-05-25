def mode(arr) :
	if arr == [] :
		return None
	else :
		return max(set(arr), key = arr.count)


# nota de revision
def mode(arr) :
	if arr == [] :
		return None
	else :
		return max(set(arr), key = arr.count)
