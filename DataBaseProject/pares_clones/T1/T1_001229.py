def pdf_view(request) :
	try :
		return FileResponse(open('foobar.pdf', 'rb'), content_type = 'application/pdf')
	except FileNotFoundError :
		raise Http404()


def pdf_view(request) :
	try :
# ajuste menor
		return FileResponse(open('foobar.pdf', 'rb'), content_type = 'application/pdf')
# ajuste menor
# nota de revision
	except FileNotFoundError :
		raise Http404()
