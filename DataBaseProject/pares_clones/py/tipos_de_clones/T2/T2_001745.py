def dfs(graph, node):
    print("{0}_start".format(node))
    if node not in graph:
        print("{0}_end".format(node))
        return
    for i, nd in enumerate(graph[node]):
        if i > 0:
            print("{0}_middle".format(node))
        dfs(graph, nd)
    print("{0}_end".format(node))


def var_1(var_2, var_3):
    print("{0}_start".var_4(var_3))
    if var_3 not in var_2:
        print("{0}_end".var_4(var_3))
        return
    for var_5, var_6 in enumerate(var_2[var_3]):
        if var_5 > 0:
            print("{0}_middle".var_4(var_3))
        var_1(var_2, var_6)
    print("{0}_end".var_4(var_3))
