def mergeSort(alist) :
	print ("Splitting ", alist)
	if len(alist) > 1 :
		mid = len(alist) / / 2
		lefthalf = alist [: mid]
		righthalf = alist [mid :]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i = 0
		j = 0
		k = 0
		while i < len(lefthalf) and j < len(righthalf) :
			if lefthalf [i] < righthalf [j] :
				alist [k] = lefthalf [i]
				i = i + 1
			else :
				alist [k] = righthalf [j]
				j = j + 1
			k = k + 1
		while i < len(lefthalf) :
			alist [k] = lefthalf [i]
			i = i + 1
			k = k + 1
		while j < len(righthalf) :
			alist [k] = righthalf [j]
			j = j + 1
			k = k + 1
	print ("Merging ", alist)


def var_1(var_2) :
	print ("Splitting ", var_2)
	if len(var_2) > 1 :
		var_3 = len(var_2) / / 2
		var_4 = var_2 [: var_3]
		var_5 = var_2 [var_3 :]
		var_1(var_4)
		var_1(var_5)
		var_6 = 0
		var_7 = 0
		var_8 = 0
		while var_6 < len(var_4) and var_7 < len(var_5) :
			if var_4 [var_6] < var_5 [var_7] :
				var_2 [var_8] = var_4 [var_6]
				var_6 = var_6 + 1
			else :
				var_2 [var_8] = var_5 [var_7]
				var_7 = var_7 + 1
			var_8 = var_8 + 1
		while var_6 < len(var_4) :
			var_2 [var_8] = var_4 [var_6]
			var_6 = var_6 + 1
			var_8 = var_8 + 1
		while var_7 < len(var_5) :
			var_2 [var_8] = var_5 [var_7]
			var_7 = var_7 + 1
			var_8 = var_8 + 1
	print ("Merging ", var_2)
