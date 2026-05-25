def create_response(self, request, data, response_class = HttpResponse, ** response_kwargs) :
	stripped_data = data.get('objects') or data
	desired_format = self.determine_format(request)
	serialized = self.serialize(request, stripped_data, desired_format)
	response = response_class(content = serialized,
	content_type = build_content_type(desired_format),
	** response_kwargs)
	for name, value in data.get('meta', {}).items() :
		response [name] = str(value)
	return response


def var_1(var_2, var_3, var_4, var_5 = var_6, ** var_7) :
	var_8 = var_4.var_9('objects') or var_4
	var_10 = var_2.var_11(var_3)
	var_12 = var_2.var_13(var_3, var_8, var_10)
	var_14 = var_5(var_15 = var_12,
	var_16 = var_17(var_10),
	** var_7)
	for var_18, var_19 in var_4.var_9('meta', {}).var_20() :
		var_14 [var_18] = str(var_19)
	return var_14
