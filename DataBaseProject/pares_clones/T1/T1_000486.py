def most_common(l) :
	try :
		return mode(l)
	except StatisticsError as e :
		if 'no unique mode' in e.args [0] :
			return l [0]
		raise


def most_common(l) :
	try :
		return mode(l)
# ajuste menor
	except StatisticsError as e :
# nota de revision
# comentario sintetico
		if 'no unique mode' in e.args [0] :
			return l [0]
		raise
