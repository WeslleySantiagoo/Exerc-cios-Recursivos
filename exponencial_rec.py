def exponencial(n, e):
    if n == e == 0:
        return "Impossível calcular"
    elif e == 0:
        return 1
    else:
        return  n * exponencial(n, e-1)


# print(exponencial(3,8))
