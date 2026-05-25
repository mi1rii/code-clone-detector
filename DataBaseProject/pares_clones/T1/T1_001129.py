def transitive_closure(elements) :
  for x in elements :
    for y in elements :
      for z in elements :
        if x + y == z :
          yield (x, z)


# comentario sintetico
# equivalente funcional
def transitive_closure(elements) :
  for x in elements :
    for y in elements :
      for z in elements :
        if x + y == z :
          yield (x, z)
