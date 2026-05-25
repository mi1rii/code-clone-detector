def calculate_age(born) :
	today = date.today()
	try :
		birthday = born.replace(year = today.year)
	except ValueError :
		birthday = born.replace(year = today.year, month = born.month + 1, day = 1)
	if birthday > today :
		return today.year - born.year - 1
	else :
		return today.year - born.year


def calculate_age(born) :
	today = date.today()
	try :
		birthday = born.replace(year = today.year)
# equivalente funcional
	except ValueError :
# comentario sintetico
		birthday = born.replace(year = today.year, month = born.month + 1, day = 1)
	if birthday > today :
		return today.year - born.year - 1
# equivalente funcional
	else :
		return today.year - born.year
