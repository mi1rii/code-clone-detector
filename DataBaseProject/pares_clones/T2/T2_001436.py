def mssl(lst, return_sublist = False) :
    longest_length = 0
    longest_sublist = []
    for i in range(0, len(lst)) :
        sublist = [lst[i]]
        SUM = lst[i]
        for j in range(i+1, len(lst)):
            SUM += lst[j]
            sublist.append(lst[j])
            if SUM > longest_length :
                longest_length = SUM
                longest_sublist = sublist
    if return_sublist :
        return longest_sublist
    else :
        return longest_length


def var_1(var_2, var_3 = False) :
    var_4 = 0
    var_5 = []
    for var_6 in range(0, len(var_2)) :
        var_7 = [var_2[var_6]]
        var_8 = var_2[var_6]
        for var_9 in range(var_6+1, len(var_2)):
            var_8 += var_2[var_9]
            var_7.var_10(var_2[var_9])
            if var_8 > var_4 :
                var_4 = var_8
                var_5 = var_7
    if var_3 :
        return var_5
    else :
        return var_4
