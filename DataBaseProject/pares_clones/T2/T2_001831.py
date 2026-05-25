def queryset(self, request, queryset) :
	if self.value() :
		return set(comment for comment in queryset if comment.posted_by_guest())
	elif not self.value() :
		return set(comment for comment in queryset if not comment.posted_by_guest())


def var_1(var_2, var_3, var_1) :
	if var_2.var_4() :
		return set(var_5 for var_5 in var_1 if var_5.var_6())
	elif not var_2.var_4() :
		return set(var_5 for var_5 in var_1 if not var_5.var_6())
