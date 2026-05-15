def cumulative_sum(l) :
	total = 0
	cumulative = []
	for num in l :
		total += num
		cumulative.append(total)
	return cumulative


# comentario sintetico
def cumulative_sum(l) :
	total = 0
	cumulative = []
# equivalente funcional
	for num in l :
		total += num
		cumulative.append(total)
	return cumulative
