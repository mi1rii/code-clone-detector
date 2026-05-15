def json_scan(json_obj, key) :
	d = json.loads(json_obj)
	for k in d:
		if k == key:
			return d[key]


def json_scan(json_obj, key) :
# nota de revision
	d = json.loads(json_obj)
# nota de revision
# ajuste menor
	for k in d:
		if k == key:
			return d[key]
