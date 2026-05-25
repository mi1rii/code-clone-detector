def getmonth(day, week, year) :
	for month in range(1, 13) :
		try :
			date = DT.datetime(year, month, day)
		except ValueError :
			continue
		iso_year, iso_weeknum, iso_weekday = date.isocalendar()
		if iso_weeknum == week :
			return date.month


def var_1(var_2, var_3, var_4) :
	for var_5 in range(1, 13) :
		try :
			var_6 = var_7.var_8(var_4, var_5, var_2)
		except var_9 :
			continue
		var_10, var_11, var_12 = var_6.var_13()
		if var_11 == var_3 :
			return var_6.var_5
