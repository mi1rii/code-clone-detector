def age_in_years(from_date, to_date = datetime.date.today()) :
	if (DEBUG) :
		print("Calculate the age in years from date "+from_date+" to date "+to_date)
	year_dif = to_date.year - from_date.year
	mon_dif = to_date.month - from_date.month
	day_dif = to_date.day - from_date.day
	
	if (day_dif < 0) :
		mon_dif -= 1
	if (mon_dif < 0) :
		year_dif -= 1
	
	return year_dif


def var_1(var_2, var_3 = var_4.var_5.var_6()) :
	if (var_7) :
		print("Calculate the age in years from date "+var_2+" to date "+var_3)
	var_8 = var_3.var_9 - var_2.var_9
	var_10 = var_3.var_11 - var_2.var_11
	var_12 = var_3.var_13 - var_2.var_13
 
	if (var_12 < 0) :
		var_10 -= 1
	if (var_10 < 0) :
		var_8 -= 1
 
	return var_8
