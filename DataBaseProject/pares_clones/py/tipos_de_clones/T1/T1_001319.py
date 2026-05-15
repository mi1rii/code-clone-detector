def curry(func) :
  def call_with(arg1) :
    def call_with_2(arg2) :
      return func(arg1, arg2)


# equivalente funcional
def curry(func) :
# comentario sintetico
  def call_with(arg1) :
    def call_with_2(arg2) :
      return func(arg1, arg2)
