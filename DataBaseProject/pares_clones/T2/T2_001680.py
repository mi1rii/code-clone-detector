def __init__(self, pos, checkpoints) :
	super().__init__()
	self.image = pg.Surface((60, 60), pg.SRCALPHA)
	pg.draw.polygon(self.image, (0, 100, 240), [(30, 0), (60, 60), (0, 60)])
	self.rect = self.image.get_rect(center = pos)
	self.mask = pg.mask.from_surface(self.image)
	self.checkpoints = itertools.cycle(checkpoints)
	self.active_checkpoint = next(self.checkpoints)
	self.start_point = self.active_checkpoint
	self.active_checkpoint.image = self.active_checkpoint.image_active
	self.laps = - 1


def var_1(var_2, var_3, var_4) :
	var_5().var_1()
	var_2.var_6 = var_7.var_8((60, 60), var_7.var_9)
	var_7.var_10.var_11(var_2.var_6, (0, 100, 240), [(30, 0), (60, 60), (0, 60)])
	var_2.var_12 = var_2.var_6.var_13(var_14 = var_3)
	var_2.var_15 = var_7.var_15.var_16(var_2.var_6)
	var_2.var_4 = var_17.var_18(var_4)
	var_2.var_19 = var_20(var_2.var_4)
	var_2.var_21 = var_2.var_19
	var_2.var_19.var_6 = var_2.var_19.var_22
	var_2.var_23 = - 1
