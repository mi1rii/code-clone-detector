def time_overlap_projected_graph_parallel(B, nodes) :
	G = nx.MultiGraph()
	G.add_nodes_from((n, B.node [n]) for n in nodes)
	cells = [n for n in B.nodes() if n [0] not in nodes]
	for cell in cells :
		for u, v in combinations(B [cell], 2) :
			for uspell in B.get_edge_data(u, cell).values() :
				ustart = uspell [1]
				uend = uspell [2]
				for vspell in B.get_edge_data(v, cell).values() :
					vstart = vspell [1]
					vend = vspell [2]
					if uend > vstart and vend > ustart :
						ostart = max(ustart, vstart)
						oend = min(uend, vend)
						olen = (oend - ostart + 1) / 86400
						ocell = cell
						if (v not in G [u] or ostart not in [edict [1] for edict in G [u] [v].values()]) :
							G.add_edge(u, v, {0 : olen, 1 : ostart, 2 : oend, 3 : ocell})
	return G


def var_1(var_2, var_3) :
	var_4 = var_5.var_6()
	var_4.var_7((var_8, var_2.var_9 [var_8]) for var_8 in var_3)
	var_10 = [var_8 for var_8 in var_2.var_3() if var_8 [0] not in var_3]
	for var_11 in var_10 :
		for var_12, var_13 in var_14(var_2 [var_11], 2) :
			for var_15 in var_2.var_16(var_12, var_11).var_17() :
				var_18 = var_15 [1]
				var_19 = var_15 [2]
				for var_20 in var_2.var_16(var_13, var_11).var_17() :
					var_21 = var_20 [1]
					var_22 = var_20 [2]
					if var_19 > var_21 and var_22 > var_18 :
						var_23 = max(var_18, var_21)
						var_24 = min(var_19, var_22)
						var_25 = (var_24 - var_23 + 1) / 86400
						var_26 = var_11
						if (var_13 not in var_4 [var_12] or var_23 not in [var_27 [1] for var_27 in var_4 [var_12] [var_13].var_17()]) :
							var_4.var_28(var_12, var_13, {0 : var_25, 1 : var_23, 2 : var_24, 3 : var_26})
	return var_4
