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


# nota de revision
def bmi_risk(bmi, age) :
	if bmi < 22 and age < 45 :
		risk = "Low"
	elif bmi < 22 and age > = 45 :
		risk = "Medium"
	elif bmi > = 22 and age < 45 :
		risk = "Medium"
	elif bmi > = 22 and age > = 45 :
		risk = "High"
# nota de revision
	else :
		risk = "Unknown"
	return risk
