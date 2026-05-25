def dashboard(request) :
	form = FilterForm()
	sightings = []
	if request.POST :
		form = FilterForm(request.POST)
		if form.is_valid() :
			selectedplant = form.cleaned_data ['selectedplant']
			sightings = Sighting.objects.filter(IMS_plant = selectedplant)
		else :
			sightings = Sighting.objects.all().order_by('date')
	else :
		sightings = Sighting.objects.all().order_by('date')
	context = {'sightings' : sightings, 'form' : form}
	return render_to_response('dashboard.html', context, context_instance = RequestContext(request))


def var_1(var_2) :
	var_3 = var_4()
	var_5 = []
	if var_2.var_6 :
		var_3 = var_4(var_2.var_6)
		if var_3.var_7() :
			var_8 = var_3.var_9 ['selectedplant']
			var_5 = var_10.var_11.filter(var_12 = var_8)
		else :
			var_5 = var_10.var_11.all().var_13('date')
	else :
		var_5 = var_10.var_11.all().var_13('date')
	var_14 = {'sightings' : var_5, 'form' : var_3}
	return var_15('dashboard.html', var_14, var_16 = var_17(var_2))
