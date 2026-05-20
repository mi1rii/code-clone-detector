int factorial(int n) {
    int f = 1;
    int i;
    i = 1;
    while (i <= n) {
        f = f * i;
        i += 1;
    }
    return f;
}