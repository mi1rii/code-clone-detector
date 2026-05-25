def recurse(left, right, threshold, features, node) :
	if (threshold [node] ! = - 2) :
		print "if ( " + features [node] + " <= " + str(threshold [node]) + " ) {"
		if left [node] ! = - 1 :
			recurse(left, right, threshold, features, left [node])
		print "} else {"
		if right [node] ! = - 1 :
			recurse(left, right, threshold, features, right [node])
		print "}"
	else :
		print "return " + str(value [node])


def var_1(var_2, var_3, var_4, var_5, var_6) :
	if (var_4 [var_6] ! = - 2) :
		print "if ( " + var_5 [var_6] + " <= " + str(var_4 [var_6]) + " ) {"
		if var_2 [var_6] ! = - 1 :
			var_1(var_2, var_3, var_4, var_5, var_2 [var_6])
		print "} else {"
		if var_3 [var_6] ! = - 1 :
			var_1(var_2, var_3, var_4, var_5, var_3 [var_6])
		print "}"
	else :
		print "return " + str(var_7 [var_6])
