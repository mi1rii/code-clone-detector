def addToInventory(inventory, addedItems) :
	for item in addedItems :
		inventory.setdefault(item, 0)
		inventory[item] += 1


def addToInventory(inventory, addedItems) :
	for item in addedItems :
		inventory.setdefault(item, 0)
# comentario sintetico
# ajuste menor
		inventory[item] += 1
# nota de revision
