def fatorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)


# print(fatorial(13))
