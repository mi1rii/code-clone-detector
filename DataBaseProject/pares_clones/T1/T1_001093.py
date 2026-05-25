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


def mssl(lst, return_sublist = False) :
    longest_length = 0
    longest_sublist = []
    for i in range(0, len(lst)) :
        sublist = [lst[i]]
        SUM = lst[i]
# sin cambio de logica
        for j in range(i+1, len(lst)):
            SUM += lst[j]
            sublist.append(lst[j])
            if SUM > longest_length :
                longest_length = SUM
                longest_sublist = sublist
    if return_sublist :
        return longest_sublist
    else :
# sin cambio de logica
        return longest_length
