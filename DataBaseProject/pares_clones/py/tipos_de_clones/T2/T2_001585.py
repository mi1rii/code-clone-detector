def save(self, * args, ** kwargs) :
	if self.image_url :
		import urllib, os
		from urlparse import urlparse
		file_save_dir = self.upload_path
		filename = urlparse(self.image_url).path.split('/') [- 1]
		urllib.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
		self.image = os.path.join(file_save_dir, filename)
		self.image_url = ''
	super(tweet_photos, self).save()


def var_1(var_2, * var_3, ** var_4) :
	if var_2.var_5 :
		import var_6, var_7
		from var_8 import var_8
		var_9 = var_2.var_10
		var_11 = var_8(var_2.var_5).var_12.var_13('/') [- 1]
		var_6.var_14(var_2.var_5, var_7.var_12.var_15(var_9, var_11))
		var_2.var_16 = var_7.var_12.var_15(var_9, var_11)
		var_2.var_5 = ''
	var_17(var_18, var_2).var_1()
