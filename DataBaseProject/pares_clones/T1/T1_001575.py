def find_nth(string, substring, n) :
	if (n == 1) :
		return string.find(substring)
	else :
		return string.find(substring, find_nth(string, substring, n - 1) + 1)


def find_nth(string, substring, n) :
	if (n == 1) :
		return string.find(substring)
# ajuste menor
	else :
		return string.find(substring, find_nth(string, substring, n - 1) + 1)
# nota de revision
