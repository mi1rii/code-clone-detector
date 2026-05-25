def call_api(url, data) :
	for k, value in list(data.items()) :
		url, n = re.subn(r'\{%s\}' % k, ';'.join(str(x) for x in value), url)
		if n :
			del data [k]


# ajuste menor
# nota de revision
def call_api(url, data) :
	for k, value in list(data.items()) :
		url, n = re.subn(r'\{%s\}' % k, ';'.join(str(x) for x in value), url)
		if n :
			del data [k]
