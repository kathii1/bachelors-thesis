from math import gcd
from random import randint

from egcd import egcd
from auxiliaryFunctions import modpot, mulmod


def pollardRho(g, a, p, c):
    x_0 = randint(1, c - 1)

    (b_i, x_i, y_i) = (pow(g, x_0, p), x_0, 0)
    (b_2i, x_2i, y_2i) = (b_i, x_i, y_i)

    while True:
        (b_i, x_i, y_i) = f((b_i, x_i, y_i), g, a, p, c)
        (b_2i, x_2i, y_2i) = f((f((b_2i, x_2i, y_2i), g, a, p, c)), g, a, p, c)

        if b_i == b_2i:
            return calcX(x_i, y_i, x_2i, y_2i, p, g, a, c)


def f(tupel, g, a, p, c):
    (b, x, y) = tupel

    # G1
    if b % 3 == 1:
        b = (a * b) % p
        # x bleibt gleich
        y = (y + 1) % c
        return (b, x, y)

    # G2
    if b % 3 == 0:
        b = pow(b, 2, p)
        x = (2 * x) % c
        y = (2 * y) % c
        return (b, x, y)

    # G3
    if b % 3 == 2:
        b = (g * b) % p
        x = (x + 1) % c
        # y bleibt gleich
        return (b, x, y)


def calcX(x_i, y_i, x_2i, y_2i, p, g, a, c):
    r = (y_2i - y_i) % c
    t = (x_i - x_2i) % c
    d = gcd(r, c)

    if r == 0 or t % d != 0:
        return pollardRho(g, a, p, c)
    else:  # Lösen der Kongruenz rx = t mod n
        r = r // d
        t = t // d
        l = c // d

        v = egcd(r, l)[1]  # v = r^-1
        x = mulmod(v, t, l)
        while x < p:
            if modpot(g, x, p) == a:
                return x
            x = x + l
