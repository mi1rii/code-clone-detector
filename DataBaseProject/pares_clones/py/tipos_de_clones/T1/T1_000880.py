def get_leaves(self, node) :
	kids = getchildren(node)
	for i in kids :
		if leafnode(i) :
			self.get_leaves(i)
		else :
			a = process_leaf(i)
			self.list_of_leaves.append(a)


def get_leaves(self, node) :
	kids = getchildren(node)
	for i in kids :
# sin cambio de logica
		if leafnode(i) :
			self.get_leaves(i)
# comentario sintetico
		else :
			a = process_leaf(i)
			self.list_of_leaves.append(a)
