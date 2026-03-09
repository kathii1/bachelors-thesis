import math
from egcd import egcd
from primefac import isprime
from random import randint
from math import sqrt, log
from numpy import empty, gcd, copy, int64

from auxiliaryFunctions import mulmod


def indexCalculus(g, h, p, c):
    B = int(math.exp((1 / sqrt(2)) * (log(c) ** (1 / 2)) * ((log(log(c))) ** (1 / 2))))
    F_B = createFactorbasis(B)
    m = len(F_B)

    # Erstellen der Relationenmatrix
    t = 1
    M = empty(shape=(m + t, m + 2), dtype='int64')
    for i in range(m + t):
        M[i] = createRelation(g, h, p, c, F_B)

    # Bringe Matrix M mod p in Zeilen-Stufen-Form
    works = rowEchelonForm(M, c)
    a = int64(M[len(M) - 1, len(M[0]) - 2])
    b = int64(M[len(M) - 1, len(M[0]) - 1])
    if b == 0 or gcd(c, b) != 1 or not works:
        return indexCalculus(g, h, p, c)
    else:
        x = mulmod(-a, (egcd(b, c)[1]) % c, c)
        return x


# Sucht Relationen mit g^a*h^b B-glatt
def createRelation(g, h, p, c, F_B):
    m = len(F_B)
    rel = empty(shape=m + 2, dtype='int64')
    while True:
        a = randint(0, c - 1)
        b = randint(0, c - 1)
        d = (pow(g, a, p) * pow(h, b, p)) % p
        # Probedivision
        j = 0
        for q in F_B:
            exp = 0
            while d % q == 0:
                d = d // q
                exp += 1
            rel[j] = exp
            j += 1
        rel[m] = a
        rel[m + 1] = b
        if d == 1:
            return rel


# Stellt die Faktorbasis F(B) zur Schranke B auf
def createFactorbasis(B):
    F_B = []
    for x in range(2, B + 1):
        if isprime(x):
            F_B.append(x)
    return F_B


def rowEchelonForm(M, c):
    row = 0
    col = 0
    rows = len(M)
    cols = len(M[0])

    while row < rows - 1 and col < cols - 2:
        # Suche Pivot-Element
        t = gcd(c, int64(M[row, col]))
        if t != 1:
            for r in range(row + 1, rows):
                t = gcd(c, int64(M[r, col]))
                if t == 1:
                    # Zeilentausch
                    temp = copy(M[r])
                    M[r] = copy(M[row])
                    M[row] = temp
                    break
            # Falls kein Pivot-Element, prüfe, ob alle Elemente der Spalte 0 sind
            if t != 1:
                for r in range(row + 1, rows):
                    if int64(M[r, col]) != 0:
                        return False
                col += 1
                continue

        # Mit dem Pivot-Element in den darunterliegenden Elementen der Spalte Nullen erzeugen
        d = (egcd(int64(M[row, col]), c)[1]) % c
        for i in range(row + 1, rows):
            x = mulmod(int64(-M[i, col]), d, c)
            M[i] = (M[i] + mulmod(M[row], x, c)) % c  # x-Faches der Zeile M[row] wird zur Zeile i addiert
        col += 1
        row += 1
    return True
