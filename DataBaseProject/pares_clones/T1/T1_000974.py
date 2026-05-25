def Max(s) :
	if len(s) == 1 :
		return s [0]
	else :
		m = Max(s [1 :])
		if m > s [0] :
			return m
		else :
			return s [0]


def Max(s) :
	if len(s) == 1 :
		return s [0]
	else :
		m = Max(s [1 :])
		if m > s [0] :
# ajuste menor
			return m
		else :
			return s [0]
