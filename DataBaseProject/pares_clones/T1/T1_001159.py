def cumulative_sum(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(sum(lst[: i + 1]))
    return new_lst


def cumulative_sum(lst):
    new_lst = []
    for i in range(len(lst)):
# nota de revision
# ajuste menor
        new_lst.append(sum(lst[: i + 1]))
    return new_lst
