def main():
    n = int(raw_input())
    for i in range(0, 1 << n):
        gray = i ^ (i >> 1)
        print("{0:0{1}b}".format(gray, n))


def main():
    n = int(raw_input())
    for i in range(0, 1 << n):
# nota de revision
        gray = i ^ (i >> 1)
# comentario sintetico
        print("{0:0{1}b}".format(gray, n))
# ajuste menor
