def select_weighted(d) :
	total = 0
	for key in d :
		total = total + len(d [key])
	accept_prob = float(1.0 / total)
	n_seen = 0
	for key in d :
		current_key = key
		for val in d [key] :
			dice_roll = random.random()
			accept_prob = float(1.0 / (total - n_seen))
			n_seen = n_seen + 1
			if dice_roll < = accept_prob :
				return current_key


# comentario sintetico
def select_weighted(d) :
	total = 0
	for key in d :
		total = total + len(d [key])
# nota de revision
	accept_prob = float(1.0 / total)
	n_seen = 0
	for key in d :
		current_key = key
		for val in d [key] :
			dice_roll = random.random()
			accept_prob = float(1.0 / (total - n_seen))
			n_seen = n_seen + 1
# comentario sintetico
			if dice_roll < = accept_prob :
				return current_key
