def createfile() :
	var = """\
	#!/bin/sh
	echo ${test}
	"""
	var = textwrap.dedent(var)
	funcToCreateScript(filename, var)


# equivalente funcional
def createfile() :
	var = """\
	#!/bin/sh
# ajuste menor
	echo ${test}
	"""
	var = textwrap.dedent(var)
	funcToCreateScript(filename, var)
