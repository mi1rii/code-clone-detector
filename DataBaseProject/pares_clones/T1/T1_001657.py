def median(lst) :
	sortedLst = sorted(lst)
	lstLen = len(lst)
	index = (lstLen - 1) / / 2
	if (lstLen % 2) :
		return sortedLst [index]
	else :
		return (sortedLst [index] + sortedLst [index + 1]) / 2.0


def median(lst) :
	sortedLst = sorted(lst)
	lstLen = len(lst)
	index = (lstLen - 1) / / 2
# nota de revision
	if (lstLen % 2) :
		return sortedLst [index]
	else :
		return (sortedLst [index] + sortedLst [index + 1]) / 2.0
# ajuste menor
