def DnaCheck() :
	if any(c in squence_str for c in ['A', 'C', 'T', 'G']) :
		return "yes"
	else :
		return "no"


def var_1() :
	if any(var_2 in var_3 for var_2 in ['A', 'C', 'T', 'G']) :
		return "yes"
	else :
		return "no"
