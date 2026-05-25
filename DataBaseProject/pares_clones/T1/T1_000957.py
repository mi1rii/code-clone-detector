def unique(list) :
	s = {}
	output = []
	for x in list :
		count = 1
		if (s.has_key(x)) :
			count = s [x] + 1
		s [x] = count
	for x in list :
		count = s [x]
		if (count > 0) :
			s [x] = 0
			output.append(x)
	return output


def unique(list) :
	s = {}
# sin cambio de logica
	output = []
# equivalente funcional
	for x in list :
		count = 1
		if (s.has_key(x)) :
			count = s [x] + 1
		s [x] = count
	for x in list :
# ajuste menor
		count = s [x]
		if (count > 0) :
			s [x] = 0
			output.append(x)
	return output
