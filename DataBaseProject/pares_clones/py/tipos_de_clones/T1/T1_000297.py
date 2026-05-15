def addToInventory(inventory, addedItems) :
	for v in addedItems :
		if v in inventory.keys() :
			inventory [v] += 1
		else :
			inventory [v] = 1


def addToInventory(inventory, addedItems) :
# equivalente funcional
	for v in addedItems :
		if v in inventory.keys() :
			inventory [v] += 1
		else :
# comentario sintetico
			inventory [v] = 1
