from math import gcd
from random import randint


# Berechnet x in h = g^x mod n
def pollardRho(g, a, p):
    n = p - 1
    x_0 = randint(1, n)

    (b_i, x_i, y_i) = (pow(g, x_0, p), x_0, 0)
    (b_2i, x_2i, y_2i) = (b_i, x_i, y_i)

    while True:
        (b_i, x_i, y_i) = f((b_i, x_i, y_i), g, a, p, n)
        (b_2i, x_2i, y_2i) = f((f((b_2i, x_2i, y_2i), g, a, p, n)), g, a, p, n)

        if b_i == b_2i:
            return calcX(x_i, y_i, x_2i, y_2i, p, n, g, a)


def f(tuple, g, a, p, n):
    (b, x, y) = tuple

    # G1
    if b % 3 == 1:
        b = (a * b) % p
        # x bleibt gleich
        y = (y + 1) % n
        return (b, x, y)

    # G2
    if b % 3 == 0:
        b = pow(b, 2, p)
        x = (2 * x) % n
        y = (2 * y) % n
        return (b, x, y)

    # G3
    if b % 3 == 2:
        b = (g * b) % p
        x = (x + 1) % n
        # y bleibt gleich
        return (b, x, y)


def calcX(x_i, y_i, x_2i, y_2i, p, n, g, a):
    r = (y_2i - y_i) % n
    t = (x_i - x_2i) % n
    d = gcd(r, n)

    if r == 0 or t % d != 0:
        return pollardRho(g, a, p)
    else:  # Lösen der Kongruenz rx = t mod n
        r = r // d
        t = t // d
        l = n // d

        v = pow(r, -1, l)  # v = r^-1
        x = v * t % l
        while x < p:
            if pow(g, x, p) == a:
                return x
            x = x + l


# Challenges
if __name__ == '__main__':
    print("Ergebnis mit Pollard-Rho zu 1) p = 1000000007,  g = 5,  a = 956753877: ",
          pollardRho(5, 956753877, 1000000007))
    print("Ergebnis mit Pollard-Rho zu 2) p = 1000000000039,  g = 3,  a = 553148792254: ",
          pollardRho(3, 553148792254, 1000000000039))
    print("Ergebnis mit Pollard-Rho zu 3) p = 1000000000000037,  g = 2,  a = 531451537204691: ",
          pollardRho(2, 531451537204691, 1000000000000037))
    print("Ergebnis zu mit Pollard-Rho 4) p = 1000000000000000003,  g = 2,  a = 849190343074049585: ",
          pollardRho(2, 849190343074049585, 1000000000000000003))
