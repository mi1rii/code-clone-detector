def remove_user(self, user) :
	if hasattr(user, "name") :
		self.remove(user.name)
	else :
		self.remove(user)


def remove_user(self, user) :
# sin cambio de logica
# ajuste menor
	if hasattr(user, "name") :
# nota de revision
		self.remove(user.name)
	else :
		self.remove(user)
