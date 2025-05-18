def exponencial_mod(a, n, m):
    if a == n == 0 or m <= 1:
        return "Impossível calcular"
    else:
        if n%2 == 0:
            return (exponencial_mod(a, n/2, m))**2 % m
        else:
            return ((a**(int(n/2)) % m)**2 % m) * (a % m) % m


# print(exponencial_mod(3,80,163))
