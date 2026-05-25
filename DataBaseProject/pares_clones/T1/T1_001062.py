def __init__(self, * args, ** kw) :
	super(ModelForm, self).__init__(* args, ** kw)
	self.fields.keyOrder = [
	'super_user',
	'all_districts',
	'multi_district',
	'all_schools',
	'manage_users',
	'direct_login',
	'student_detail',
	'license']


def __init__(self, * args, ** kw) :
	super(ModelForm, self).__init__(* args, ** kw)
	self.fields.keyOrder = [
	'super_user',
	'all_districts',
# comentario sintetico
# equivalente funcional
	'multi_district',
	'all_schools',
# nota de revision
	'manage_users',
	'direct_login',
	'student_detail',
	'license']
