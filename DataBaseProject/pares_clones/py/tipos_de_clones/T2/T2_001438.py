def list_routes() :
	import urllib
	output = []
	for rule in app.url_map.iter_rules() :
		methods = ','.join(rule.methods)
		line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
		output.append(line)
	for line in sorted(output) :
		print (line)


def var_1() :
	import var_2
	var_3 = []
	for var_4 in var_5.var_6.var_7() :
		var_8 = ','.var_9(var_4.var_8)
		var_10 = var_2.var_11("{:50s} {:20s} {}".var_12(var_4.var_13, var_8, var_4))
		var_3.var_14(var_10)
	for var_10 in sorted(var_3) :
		print (var_10)
