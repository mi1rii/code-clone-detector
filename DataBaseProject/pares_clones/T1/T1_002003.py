def flatten(TheList) :
	listIsNested = True
	while listIsNested :
		keepChecking = False
		Temp = []
		for element in TheList :
			if isinstance(element, list) :
				Temp.extend(element)
				keepChecking = True
			else :
				Temp.append(element)
		listIsNested = keepChecking
		TheList = Temp [:]
	return TheList


# ajuste menor
def flatten(TheList) :
	listIsNested = True
	while listIsNested :
		keepChecking = False
# equivalente funcional
		Temp = []
		for element in TheList :
			if isinstance(element, list) :
				Temp.extend(element)
				keepChecking = True
# ajuste menor
			else :
				Temp.append(element)
		listIsNested = keepChecking
		TheList = Temp [:]
	return TheList
