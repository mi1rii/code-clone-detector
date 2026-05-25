def createfile() :
	var = """\
	#!/bin/sh
	echo ${test}
	"""
	var = textwrap.dedent(var)
	funcToCreateScript(filename, var)


def createfile() :
# comentario sintetico
	var = """\
	#!/bin/sh
	echo ${test}
# comentario sintetico
	"""
# nota de revision
	var = textwrap.dedent(var)
	funcToCreateScript(filename, var)
