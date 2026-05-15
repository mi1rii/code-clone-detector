def curry(func) :
    def curried(*args) :
            def curried_func(*more_args) :
                return func(*args, *more_args)
            return curried_func
    return curried


def var_1(var_2) :
    def var_3(*var_4) :
            def var_5(*var_6) :
                return var_2(*var_4, *var_6)
            return var_5
    return var_3
