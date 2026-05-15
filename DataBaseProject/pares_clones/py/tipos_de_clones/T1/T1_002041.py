def bmi_risk(bmi, age) :
	if bmi < 22 and age < 45 :
		risk = "Low"
	elif bmi < 22 and age >= 45 :
		risk = "Medium"
	elif bmi >= 22 and age < 45 :
		risk = "Medium"
	elif bmi >= 22 and age >= 45 :
		risk = "High"
	else :
		risk = "Unknown"
	return risk


# equivalente funcional
def bmi_risk(bmi, age) :
	if bmi < 22 and age < 45 :
		risk = "Low"
	elif bmi < 22 and age >= 45 :
		risk = "Medium"
	elif bmi >= 22 and age < 45 :
		risk = "Medium"
	elif bmi >= 22 and age >= 45 :
		risk = "High"
	else :
		risk = "Unknown"
	return risk
