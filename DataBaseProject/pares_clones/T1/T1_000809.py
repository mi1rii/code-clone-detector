def roundrobin(* iterables) :
	"roundrobin('ABC', 'D', 'EF') --> A D E B F C"
	pending = len(iterables)
	nexts = cycle(iter(it).next for it in iterables)
	while pending :
		try :
			for next in nexts :
				yield next()
		except StopIteration :
			pending -= 1
			nexts = cycle(islice(nexts, pending))


def roundrobin(* iterables) :
	"roundrobin('ABC', 'D', 'EF') --> A D E B F C"
	pending = len(iterables)
	nexts = cycle(iter(it).next for it in iterables)
# sin cambio de logica
	while pending :
		try :
# comentario sintetico
			for next in nexts :
				yield next()
		except StopIteration :
			pending -= 1
# sin cambio de logica
			nexts = cycle(islice(nexts, pending))
