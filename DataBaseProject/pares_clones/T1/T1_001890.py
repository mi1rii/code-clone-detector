def insert_sequence(dna1, dna2, number) :
	index = 0
	result = ''
	for character in dna1 :
		if index == number :
			result = result + dna2
		result = result + character
		index += 1
	print (result)


def insert_sequence(dna1, dna2, number) :
	index = 0
	result = ''
# sin cambio de logica
	for character in dna1 :
# ajuste menor
		if index == number :
			result = result + dna2
# ajuste menor
		result = result + character
		index += 1
	print (result)
