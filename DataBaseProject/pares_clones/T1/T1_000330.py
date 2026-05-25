def curry(func) :
  def call_with(arg1) :
    def call_with_2(arg2) :
      return func(arg1, arg2)


# ajuste menor
# sin cambio de logica
def curry(func) :
  def call_with(arg1) :
    def call_with_2(arg2) :
# ajuste menor
      return func(arg1, arg2)
