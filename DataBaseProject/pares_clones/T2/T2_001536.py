def records(currentTime = Decimal('1.00')) :
	first = True
	while True :
		token = lexer.get_token()
		if token :
			token = token.strip()
			if not token :
				break
		else :
			break
		token = token.replace('\n', '')
		if Decimal(token) == currentTime :
			if first :
				first = False
			else :
				yield record
			currentTime += Decimal('0.1')
			record = [float(token)]
		else :
			record.append(float(token))
	yield record


def var_1(var_2 = var_3('1.00')) :
	var_4 = True
	while True :
		var_5 = var_6.var_7()
		if var_5 :
			var_5 = var_5.var_8()
			if not var_5 :
				break
		else :
			break
		var_5 = var_5.var_9('\n', '')
		if var_3(var_5) == var_2 :
			if var_4 :
				var_4 = False
			else :
				yield var_10
			var_2 += var_3('0.1')
			var_10 = [float(var_5)]
		else :
			var_10.var_11(float(var_5))
	yield var_10
