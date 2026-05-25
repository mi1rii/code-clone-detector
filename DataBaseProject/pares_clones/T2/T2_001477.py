def previous_quarter(date) :
	date = DT.datetime(date.year, date.month, date.day)
	rr = rrule.rrule(
	rrule.DAILY,
	bymonth = (3, 6, 9, 12),
	bymonthday = - 1,
	dtstart = date - DT.timedelta(days = 100))
	result = rr.before(date, inc = False)
	return result.date()


def var_1(var_2) :
	var_2 = var_3.var_4(var_2.var_5, var_2.var_6, var_2.var_7)
	var_8 = var_9.var_9(
	var_9.var_10,
	var_11 = (3, 6, 9, 12),
	var_12 = - 1,
	var_13 = var_2 - var_3.var_14(var_15 = 100))
	var_16 = var_8.var_17(var_2, var_18 = False)
	return var_16.var_2()
