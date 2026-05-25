def curry(func) :
    def curried(*args) :
            def curried_func(*more_args) :
                return func(*args, *more_args)
            return curried_func
    return curried


# equivalente funcional
# nota de revision
def curry(func) :
    def curried(*args) :
            def curried_func(*more_args) :
                return func(*args, *more_args)
            return curried_func
# sin cambio de logica
    return curried
