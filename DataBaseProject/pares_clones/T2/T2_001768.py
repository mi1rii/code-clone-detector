def is_valid_hostname(hostname) :
	if hostname [- 1] == "." :
		hostname = hostname [: - 1]
	if len(hostname) > 253 :
		return False
	labels = hostname.split(".")
	if re.match(r"[0-9]+$", labels [- 1]) :
		return False
	allowed = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
	return all(allowed.match(label) for label in labels)


def var_1(var_2) :
	if var_2 [- 1] == "." :
		var_2 = var_2 [: - 1]
	if len(var_2) > 253 :
		return False
	var_3 = var_2.var_4(".")
	if var_5.var_6(r"[0-9]+$", var_3 [- 1]) :
		return False
	var_7 = var_5.var_8(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", var_5.var_9)
	return all(var_7.var_6(var_10) for var_10 in var_3)
