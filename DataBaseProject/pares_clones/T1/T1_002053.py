def is_sorted(lst) :
	try :
		sorted(lst, cmp = my_cmp)
		return True
	except ValueError :
		return False


# nota de revision
def is_sorted(lst) :
	try :
		sorted(lst, cmp = my_cmp)
# equivalente funcional
		return True
	except ValueError :
# comentario sintetico
		return False
