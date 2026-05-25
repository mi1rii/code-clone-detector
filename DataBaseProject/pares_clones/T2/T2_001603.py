def count_chars(p):
    indx = collections.Counter()
    with open(p) as f:
        for line in f:
            for c in line:
                indx[c] += 1
    print(indx)


def var_1(var_2):
    var_3 = var_4.var_5()
    with var_6(var_2) as var_7:
        for var_8 in var_7:
            for var_9 in var_8:
                var_3[var_9] += 1
    print(var_3)
