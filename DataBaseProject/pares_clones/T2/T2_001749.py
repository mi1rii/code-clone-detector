def compose(f, n) :
  def g(x):
    return f(n(x))
  return g


def var_1(var_2, var_3) :
  def var_4(var_5):
    return var_2(var_3(var_5))
  return var_4
