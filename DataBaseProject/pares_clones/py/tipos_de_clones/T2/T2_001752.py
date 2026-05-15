def __init__(self, pos, angle = 0) :
	super().__init__()
	self.image_inactive = pg.transform.rotate(CHECKPOINT_IMG, angle)
	self.image_active = pg.transform.rotate(CHECKPOINT2_IMG, angle)
	self.image = self.image_inactive
	self.rect = self.image.get_rect(center = pos)
	self.mask = pg.mask.from_surface(self.image)


def var_1(var_2, var_3, var_4 = 0) :
	var_5().var_1()
	var_2.var_6 = var_7.var_8.var_9(var_10, var_4)
	var_2.var_11 = var_7.var_8.var_9(var_12, var_4)
	var_2.var_13 = var_2.var_6
	var_2.var_14 = var_2.var_13.var_15(var_16 = var_3)
	var_2.var_17 = var_7.var_17.var_18(var_2.var_13)
