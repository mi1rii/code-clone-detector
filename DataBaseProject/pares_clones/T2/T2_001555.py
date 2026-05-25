def save(self, * args, ** kwargs) :
	imageTemproary = Image.open(self.uploadedImage)
	outputIoStream = BytesIO()
	imageTemproaryResized = imageTemproary.resize((1020, 573))
	imageTemproaryResized.save(outputIoStream, format = 'JPEG', quality = 85)
	outputIoStream.seek(0)
	self.uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.uploadedImage.name.split('.') [0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
	super(ImageUpload, self).save(* args, ** kwargs)


def var_1(var_2, * var_3, ** var_4) :
	var_5 = var_6.var_7(var_2.var_8)
	var_9 = var_10()
	var_11 = var_5.var_12((1020, 573))
	var_11.var_1(var_9, var_13 = 'JPEG', var_14 = 85)
	var_9.var_15(0)
	var_2.var_8 = var_16(var_9, 'ImageField', "%s.jpg" % var_2.var_8.var_17.var_18('.') [0], 'image/jpeg', var_19.var_20(var_9), None)
	var_21(var_22, var_2).var_1(* var_3, ** var_4)
