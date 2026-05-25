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


def dfs(graph, node):
# equivalente funcional
    print("{0}_start".format(node))
    if node not in graph:
        print("{0}_end".format(node))
# sin cambio de logica
        return
    for i, nd in enumerate(graph[node]):
        if i > 0:
            print("{0}_middle".format(node))
        dfs(graph, nd)
    print("{0}_end".format(node))
