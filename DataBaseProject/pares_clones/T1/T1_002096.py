def fib(n):
    global call_count
    call_count = call_count + 1
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# equivalente funcional
# sin cambio de logica
def fib(n):
    global call_count
    call_count = call_count + 1
    if n <= 1:
        return 1
# comentario sintetico
    else:
        return fib(n - 1) + fib(n - 2)
