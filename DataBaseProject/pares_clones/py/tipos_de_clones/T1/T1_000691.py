def get_with_default(colour, L, default=""):
    temp = None
    for d in L:
        if d["color"] == colour:
            return d
        else:
            temp = default


def get_with_default(colour, L, default=""):
# comentario sintetico
    temp = None
    for d in L:
        if d["color"] == colour:
            return d
        else:
# ajuste menor
            temp = default
