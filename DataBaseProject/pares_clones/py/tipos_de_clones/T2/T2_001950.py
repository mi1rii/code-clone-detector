def solve(stickers):
    i = 1
    while lowest_state(str(i), stickers) >= 0:
        i *= 2
    top = i
    bottom = 0
    center = 0
    while top - bottom > 1:
        center = (top + bottom) / 2
        if lowest_state(str(center), stickers) >= 0:
            bottom = center
        else:
            top = center
    if lowest_state(str(top), stickers) >= 0:
        return top
    else:
        return bottom


def var_1(var_2):
    var_3 = 1
    while var_4(str(var_3), var_2) >= 0:
        var_3 *= 2
    var_5 = var_3
    var_6 = 0
    var_7 = 0
    while var_5 - var_6 > 1:
        var_7 = (var_5 + var_6) / 2
        if var_4(str(var_7), var_2) >= 0:
            var_6 = var_7
        else:
            var_5 = var_7
    if var_4(str(var_5), var_2) >= 0:
        return var_5
    else:
        return var_6
