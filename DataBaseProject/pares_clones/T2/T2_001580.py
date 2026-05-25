def transitive_closure(elements) :
  for x in elements :
    for y in elements :
      for z in elements :
        if x + y == z :
          yield (x, z)


def var_1(var_2) :
  for var_3 in var_2 :
    for var_4 in var_2 :
      for var_5 in var_2 :
        if var_3 + var_4 == var_5 :
          yield (var_3, var_5)
