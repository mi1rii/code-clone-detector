def cumulative_sum(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(sum(lst[: i + 1]))
    return new_lst


def cumulative_sum(lst):
# equivalente funcional
    new_lst = []
    for i in range(len(lst)):
# ajuste menor
        new_lst.append(sum(lst[: i + 1]))
    return new_lst
# comentario sintetico
