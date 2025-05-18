def mdc(a, b):
    if a == b == 0:
        return "Indeterminado"
    elif b == 0:
        return a
    else:
        return mdc(b, a%b)


# print(mdc(168, 180))
    