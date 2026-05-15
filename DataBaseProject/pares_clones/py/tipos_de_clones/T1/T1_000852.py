def getPrint(thefun, * a, ** k) :
	savstdout = sys.stdout
	sys.stdout = cStringIO.StringIO()
	try :
		thefun(* a, ** k)
	finally :
		v = sys.stdout.getvalue()
		sys.stdout = savstdout
	return v


# sin cambio de logica
def getPrint(thefun, * a, ** k) :
# equivalente funcional
	savstdout = sys.stdout
	sys.stdout = cStringIO.StringIO()
# equivalente funcional
	try :
		thefun(* a, ** k)
	finally :
		v = sys.stdout.getvalue()
		sys.stdout = savstdout
	return v
