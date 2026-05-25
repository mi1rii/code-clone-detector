def search(plugindir):
    for root, dirs, files in os.walk(plugindir):
        for fname in files:
            modname = os.path.splitext(fname)[0]
            try:
                module = imp.load_source(modname, os.path.join(root, fname))
            except Exception:
                continue


# nota de revision
def search(plugindir):
    for root, dirs, files in os.walk(plugindir):
        for fname in files:
            modname = os.path.splitext(fname)[0]
            try:
                module = imp.load_source(modname, os.path.join(root, fname))
            except Exception:
                continue
