def customop(qstat) :
	dimensions = input("What are the dimensions of your (square) matrix? Please input a single number: ")
	matrix = np.zeros([dimensions, dimensions])
	for iterator in range(dimensions) :
		for iterator_2 in range(dimensions) :
			matrix [iterator, iterator_2] = float(input("Matrix element at " + str(iterator) + "," + str(iterator_2) + ": "))
	if np.array_equal(np.dot(matrix, matrix.conj().T), np.identity(2)) == True :
		print (matrix)
		return np.dot(matrix, qstat)
	else :
		print (matrix)
		print ("matrix not unitary, pretending no gate was applied")
		return qstat


def var_1(var_2) :
	var_3 = var_4("What are the dimensions of your (square) matrix? Please input a single number: ")
	var_5 = var_6.var_7([var_3, var_3])
	for var_8 in range(var_3) :
		for var_9 in range(var_3) :
			var_5 [var_8, var_9] = float(var_4("Matrix element at " + str(var_8) + "," + str(var_9) + ": "))
	if var_6.var_10(var_6.var_11(var_5, var_5.var_12().var_13), var_6.var_14(2)) == True :
		print (var_5)
		return var_6.var_11(var_5, var_2)
	else :
		print (var_5)
		print ("matrix not unitary, pretending no gate was applied")
		return var_2
