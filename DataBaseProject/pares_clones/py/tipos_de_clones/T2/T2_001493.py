def decorator2(method_to_decorate):
    @wraps(method_to_decorate)
    def wrapper(*args, **kwargs):
        a = args[0]
        result = method_to_decorate(*args, **kwargs)
        return result + a


def var_1(var_2):
    @var_3(var_2)
    def var_4(*var_5, **var_6):
        var_7 = var_5[0]
        var_8 = var_2(*var_5, **var_6)
        return var_8 + var_7
