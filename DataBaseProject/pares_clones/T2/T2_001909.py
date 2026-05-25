def __setitem__(self, key, value) :
	if key in self.dictionary :
		self.dictionary [key] [1] = value
		return
	if self.removed_indices is None :
		index = self.next_index
		self.next_index += 1
	else :
		index = self.removed_indices [0]
		self.removed_indices = self.removed_indices [1]
	self.dictionary [key] = [index, value]
	self.indexdict [index] = key
	self.len += 1


def var_1(var_2, var_3, var_4) :
	if var_3 in var_2.var_5 :
		var_2.var_5 [var_3] [1] = var_4
		return
	if var_2.var_6 is None :
		var_7 = var_2.var_8
		var_2.var_8 += 1
	else :
		var_7 = var_2.var_6 [0]
		var_2.var_6 = var_2.var_6 [1]
	var_2.var_5 [var_3] = [var_7, var_4]
	var_2.var_9 [var_7] = var_3
	var_2.len += 1
