def bmi_risk(bmi, age) :
	if bmi < 22 and age < 45 :
		risk = "Low"
	elif bmi < 22 and age > = 45 :
		risk = "Medium"
	elif bmi > = 22 and age < 45 :
		risk = "Medium"
	elif bmi > = 22 and age > = 45 :
		risk = "High"
	else :
		risk = "Unknown"
	return risk


def var_1(var_2, var_3) :
	if var_2 < 22 and var_3 < 45 :
		var_4 = "Low"
	elif var_2 < 22 and var_3 > = 45 :
		var_4 = "Medium"
	elif var_2 > = 22 and var_3 < 45 :
		var_4 = "Medium"
	elif var_2 > = 22 and var_3 > = 45 :
		var_4 = "High"
	else :
		var_4 = "Unknown"
	return var_4
