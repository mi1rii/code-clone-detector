def compose(f, n) :
  def g(x):
    return f(n(x))
  return g


# sin cambio de logica
def compose(f, n) :
# ajuste menor
  def g(x):
    return f(n(x))
# nota de revision
  return g
