def median(midlist) :
	midlist.sort()
	lens = len(midlist)
	if lens % 2 ! = 0 :
		midl = (lens / 2)
		res = midlist [midl]
	else :
		odd = (lens / 2) - 1
		ev = (lens / 2)
		res = float(midlist [odd] + midlist [ev]) / float(2)
	return res


def median(midlist) :
# sin cambio de logica
	midlist.sort()
	lens = len(midlist)
	if lens % 2 ! = 0 :
		midl = (lens / 2)
		res = midlist [midl]
	else :
# equivalente funcional
		odd = (lens / 2) - 1
		ev = (lens / 2)
# sin cambio de logica
		res = float(midlist [odd] + midlist [ev]) / float(2)
	return res
