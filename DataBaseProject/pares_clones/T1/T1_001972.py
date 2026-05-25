def __init__(self, pos, angle = 0) :
	super().__init__()
	self.image_inactive = pg.transform.rotate(CHECKPOINT_IMG, angle)
	self.image_active = pg.transform.rotate(CHECKPOINT2_IMG, angle)
	self.image = self.image_inactive
	self.rect = self.image.get_rect(center = pos)
	self.mask = pg.mask.from_surface(self.image)


def __init__(self, pos, angle = 0) :
	super().__init__()
	self.image_inactive = pg.transform.rotate(CHECKPOINT_IMG, angle)
# sin cambio de logica
	self.image_active = pg.transform.rotate(CHECKPOINT2_IMG, angle)
# comentario sintetico
	self.image = self.image_inactive
# comentario sintetico
	self.rect = self.image.get_rect(center = pos)
	self.mask = pg.mask.from_surface(self.image)
