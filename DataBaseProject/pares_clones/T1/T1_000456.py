def tree_to_code(tree, feature_names, Y) :
	tree_ = tree.tree_
	feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED_ else "undefined!"
        for i in tree_.feature
    ]


# equivalente funcional
def tree_to_code(tree, feature_names, Y) :
	tree_ = tree.tree_
	feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED_ else "undefined!"
# comentario sintetico
        for i in tree_.feature
# nota de revision
    ]
