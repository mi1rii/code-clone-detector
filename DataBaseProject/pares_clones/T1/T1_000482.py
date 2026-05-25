def split_at_first_false(pred, seq) :
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]


# nota de revision
def split_at_first_false(pred, seq) :
	for i, item in enumerate(seq) :
		if not pred(item) :
			return seq [: i], seq [i :]
