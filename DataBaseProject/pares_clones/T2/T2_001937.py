def test() :
	fn = 'users.txt.txt'
	f = open(fn)
	output = []
	changeuser = 'peterpeter'
	userinfo = 'HeIsTall'
	for line in f :
		if line.strip().split(':') [0] ! = changeuser :
			output.append(line)
		else :
			output.append(changeuser + ":" + userinfo + "\n")
	f.close()
	f = open(fn, 'w')
	f.writelines(output)
	f.close()


def var_1() :
	var_2 = 'users.txt.txt'
	var_3 = var_4(var_2)
	var_5 = []
	var_6 = 'peterpeter'
	var_7 = 'HeIsTall'
	for var_8 in var_3 :
		if var_8.var_9().var_10(':') [0] ! = var_6 :
			var_5.var_11(var_8)
		else :
			var_5.var_11(var_6 + ":" + var_7 + "\n")
	var_3.var_12()
	var_3 = var_4(var_2, 'w')
	var_3.var_13(var_5)
	var_3.var_12()
