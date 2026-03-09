# Berechnet (a * b) % N ohne Overflow zu erzeugen
def mulmod(a, b, N):
    if N < 10 ** 10:
        return (a * b) % N
    r = 0
    a = a % N
    while b > 0:
        if (b % 2 == 1):
            r = (r + a) % N
        a = (a * 2) % N
        b //= 2
    return r % N


# Berechnet (x ** y) % N ohne Overflow zu erzeugen
def modpot(x, y, N):
    if N < 10 ** 10:
        return pow(int(x), int(y), int(N))
    y = y % (N - 1)
    pot = 1
    while y > 0:
        if y % 2 == 1:
            pot = (pot * x) % N
            y = y - 1
        else:
            x = (x * x) % N
            y = y // 2
    return pot
