def apply_cache(request, * args, ** kwargs) :
	CACHE_KEY = cache_key(request)
	if prefix :
		CACHE_KEY = '%s_%s' % (prefix, CACHE_KEY)
	if not cache_post and request.method == 'POST' :
		can_cache = False
	else :
		can_cache = True
	if can_cache :
		response = core_cache.get(CACHE_KEY, None)
	else :
		response = None
	if not response :
		response = function(request, * args, ** kwargs)
		if can_cache :
			core_cache.set(CACHE_KEY, response, ttl)
	return response


def var_1(var_2, * var_3, ** var_4) :
	var_5 = var_6(var_2)
	if var_7 :
		var_5 = '%s_%s' % (var_7, var_5)
	if not var_8 and var_2.var_9 == 'POST' :
		var_10 = False
	else :
		var_10 = True
	if var_10 :
		var_11 = var_12.var_13(var_5, None)
	else :
		var_11 = None
	if not var_11 :
		var_11 = var_14(var_2, * var_3, ** var_4)
		if var_10 :
			var_12.set(var_5, var_11, var_15)
	return var_11
