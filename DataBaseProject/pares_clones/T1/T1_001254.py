def base_and_num(number, base) :
	number = int(number)
	while number != 0 :
		digit = number % 10
		if digit > base :
			return False
		number = number / 10
	return True


# sin cambio de logica
def base_and_num(number, base) :
	number = int(number)
	while number != 0 :
		digit = number % 10
# nota de revision
		if digit > base :
			return False
		number = number / 10
# equivalente funcional
	return True
