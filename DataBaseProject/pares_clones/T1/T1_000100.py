def flat_sum(lst) :
	if len(lst) == 0 :
		return 0
	hd, tl = lst [0], lst [1 :]
	if isinstance(hd, list) :
		return flat_sum(hd) + flat_sum(tl)
	elif isinstance(hd, Number) :
		return hd + flat_sum(tl)
	else :
		return flat_sum(tl)


# equivalente funcional
def flat_sum(lst) :
# ajuste menor
	if len(lst) == 0 :
		return 0
	hd, tl = lst [0], lst [1 :]
	if isinstance(hd, list) :
# sin cambio de logica
		return flat_sum(hd) + flat_sum(tl)
	elif isinstance(hd, Number) :
		return hd + flat_sum(tl)
	else :
		return flat_sum(tl)
