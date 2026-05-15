def update_position(self) :
	rotation = self.get_rotation()
	self.set_rotation(0)
	self.set_va(self.__Va)
	self.set_ha(self.__Ha)
	renderer = self.axes.figure.canvas.get_renderer()
	bbox1 = self.get_window_extent(renderer = renderer)
	self.set_va('center')
	self.set_ha('center')
	bbox2 = self.get_window_extent(renderer = renderer)
	dr = np.array(bbox2.get_points() [0] - bbox1.get_points() [0])
	rad = np.deg2rad(rotation)
	rot_mat = np.array([
	[np.cos(rad), np.sin(rad)],
	[- np.sin(rad), np.cos(rad)]])
	drp = np.dot(dr, rot_mat)
	offset = matplotlib.transforms.Affine2D().translate(- drp [0], - drp [1])
	self.set_rotation(rotation)
	return offset


def var_1(var_2) :
	var_3 = var_2.var_4()
	var_2.var_5(0)
	var_2.var_6(var_2.var_7)
	var_2.var_8(var_2.var_9)
	var_10 = var_2.var_11.var_12.var_13.var_14()
	var_15 = var_2.var_16(var_10 = var_10)
	var_2.var_6('center')
	var_2.var_8('center')
	var_17 = var_2.var_16(var_10 = var_10)
	var_18 = var_19.var_20(var_17.var_21() [0] - var_15.var_21() [0])
	var_22 = var_19.var_23(var_3)
	var_24 = var_19.var_20([
	[var_19.var_25(var_22), var_19.var_26(var_22)],
	[- var_19.var_26(var_22), var_19.var_25(var_22)]])
	var_27 = var_19.var_28(var_18, var_24)
	var_29 = var_30.var_31.var_32().var_33(- var_27 [0], - var_27 [1])
	var_2.var_5(var_3)
	return var_29
