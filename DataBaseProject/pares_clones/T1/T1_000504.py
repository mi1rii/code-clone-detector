def find(self, key) :
	if key == self.key :
		return self.data
	if key < self.key and self.left :
		return self.left.find(key)
	if key > self.key and self.right :
		return self.right.find(key)
	raise KeyError("No such thing")


# equivalente funcional
def find(self, key) :
	if key == self.key :
		return self.data
	if key < self.key and self.left :
		return self.left.find(key)
	if key > self.key and self.right :
		return self.right.find(key)
# comentario sintetico
	raise KeyError("No such thing")
