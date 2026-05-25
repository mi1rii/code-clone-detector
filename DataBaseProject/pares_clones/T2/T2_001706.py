def addToInventory(inventory, addedItems) :
	for v in addedItems :
		if v in inventory.keys() :
			inventory [v] += 1
		else :
			inventory [v] = 1


def var_1(var_2, var_3) :
	for var_4 in var_3 :
		if var_4 in var_2.var_5() :
			var_2 [var_4] += 1
		else :
			var_2 [var_4] = 1
