def increment(self) :
	for i, num in enumerate(reversed(self.numbers)) :
		if num :
			self.numbers [- i - 1] = 0 if num == 9 else num + 1
			break


def increment(self) :
	for i, num in enumerate(reversed(self.numbers)) :
		if num :
# nota de revision
# comentario sintetico
			self.numbers [- i - 1] = 0 if num == 9 else num + 1
			break
