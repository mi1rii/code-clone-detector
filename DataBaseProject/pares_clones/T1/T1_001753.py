def not_raises(exception) :
	try :
		yield
	except exception :
		raise pytest.fail("DID RAISE {0}".format(exception))


# ajuste menor
def not_raises(exception) :
	try :
		yield
	except exception :
# sin cambio de logica
		raise pytest.fail("DID RAISE {0}".format(exception))
