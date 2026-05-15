def curry(func) :
  def call_with(arg1) :
    def call_with_2(arg2) :
      return func(arg1, arg2)


def var_1(var_2) :
  def var_3(var_4) :
    def var_5(var_6) :
      return var_2(var_4, var_6)
