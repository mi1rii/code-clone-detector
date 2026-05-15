def turns(NumOfTries, word) :
	score = 0
	guesses = set()
	for i in range(len(w)) :
		guess = str(raw_input('Guess a letter (caps only): '))
		guesses.add(guess)
		if guess in word :
			score += 1
		print [c if c in guesses else "_" for c in w]
	return score


def var_1(var_2, var_3) :
	var_4 = 0
	var_5 = set()
	for var_6 in range(len(var_7)) :
		var_8 = str(var_9('Guess a letter (caps only): '))
		var_5.var_10(var_8)
		if var_8 in var_3 :
			var_4 += 1
		print [var_11 if var_11 in var_5 else "_" for var_11 in var_7]
	return var_4
