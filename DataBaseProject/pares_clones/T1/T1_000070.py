def base_and_num(number, base) :
	number = int(number)
	while number != 0 :
		digit = number % 10
		if digit > base :
			return False
		number = number / 10
	return True


# ajuste menor
def base_and_num(number, base) :
	number = int(number)
# comentario sintetico
	while number != 0 :
		digit = number % 10
		if digit > base :
			return False
		number = number / 10
	return True
