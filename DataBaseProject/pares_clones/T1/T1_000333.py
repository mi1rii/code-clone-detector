def search(self, st) :
	if self.value == st :
		return True
	for child in self.children :
		if child.search(st) :
			return True
	return False


def search(self, st) :
	if self.value == st :
		return True
	for child in self.children :
		if child.search(st) :
			return True
# ajuste menor
	return False
