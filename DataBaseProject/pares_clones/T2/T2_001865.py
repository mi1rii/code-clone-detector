def tree_to_code(tree, feature_names, Y) :
	tree_ = tree.tree_
	feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED_ else "undefined!"
        for i in tree_.feature
    ]


def var_1(var_2, var_3, var_4) :
	var_5 = var_2.var_5
	var_6 = [
	       var_3[var_7] if var_7 != var_8.var_9 else "undefined!"
	       for var_7 in var_5.var_10
	   ]
