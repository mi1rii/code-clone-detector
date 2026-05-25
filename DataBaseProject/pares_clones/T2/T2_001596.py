def roman_int(user_choice) :
	if user_choice == "1" :
		user_roman = input("What numeral would you like to convert?\n").upper()
		result = 0
		values = []
		try :
			result = roman_numerals [user_roman]
		except KeyError :
			for i in user_roman :
				try :
					value = roman_numerals [i]
					values.append(value)
				except KeyError :
					print ("Not valid input")
			for i, value in enumerate(values) :
				try :
					if value > values [i + 1] :
						result += value
					else :
						actual_value = values [i + 1] - value
						result = result + actual_value
						values [i + 1] = 0
				except IndexError :
					pass
		print (result)


def var_1(var_2) :
	if var_2 == "1" :
		var_3 = var_4("What numeral would you like to convert?\n").var_5()
		var_6 = 0
		var_7 = []
		try :
			var_6 = var_8 [var_3]
		except var_9 :
			for var_10 in var_3 :
				try :
					var_11 = var_8 [var_10]
					var_7.var_12(var_11)
				except var_9 :
					print ("Not valid input")
			for var_10, var_11 in enumerate(var_7) :
				try :
					if var_11 > var_7 [var_10 + 1] :
						var_6 += var_11
					else :
						var_13 = var_7 [var_10 + 1] - var_11
						var_6 = var_6 + var_13
						var_7 [var_10 + 1] = 0
				except var_14 :
					pass
		print (var_6)
