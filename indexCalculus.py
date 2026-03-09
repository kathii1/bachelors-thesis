import math
from egcd import egcd
from primefac import isprime
from random import randint
from math import sqrt, log
from numpy import empty, gcd, copy, int64
from auxiliaryFunctions import mulmod


# Berechnet x in h = g^x mod n
def indexCalculus(g, h, p):
    n = p - 1  # Ordnung von G
    B = int(math.exp((1 / sqrt(2)) * (log(n) ** (1 / 2)) * ((log(log(n))) ** (1 / 2))))
    F_B = createFactorbasis(B)
    m = len(F_B)

    # Erstellen der Relationenmatrix
    e = 1
    M = empty(shape=(m + e, m + 2), dtype='int64')
    for i in range(m + e):
        M[i] = createRelation(g, h, p, F_B)

    # Bringe Matrix M mod p in Zeilen-Stufen-Form
    works = rowEchelonForm(M, n, e)
    a = int64(M[len(M) - 1, len(M[0]) - 2])
    b = int64(M[len(M) - 1, len(M[0]) - 1])
    if b == 0 or gcd(n, b) != 1 or not works:
        for i in range(len(M)):
            # Test auf Nullzeile
            if (all(element == 0 for element in M[i, range(len(M[0]) - 2)])):
                a = int64(M[i, len(M[0]) - 2])
                b = int64(M[i, len(M[0]) - 1])
                if b == 0 or gcd(n, b) != 1:
                    continue
                else:
                    x = mulmod(-a, (egcd(b, n)[1]) % n, n)
                    return x
        return indexCalculus(g, h, p)
    else:
        x = mulmod(-a, (egcd(b, n)[1]) % n, n)
        return x


def createRelation(g, h, p, F_B):
    n = p - 1
    m = len(F_B)
    rel = empty(shape=(1, m + 2), dtype='int64')
    while True:
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        c = (pow(g, a, p) * pow(h, b, p)) % p
        # Probedivision
        j = 0
        for q in F_B:
            exp = 0
            while c % q == 0:
                c = c // q
                exp += 1
            rel[0, j] = exp
            j += 1
        rel[0, m] = a
        rel[0, m + 1] = b
        if c == 1:
            return rel


def createFactorbasis(B):
    F_B = []
    for x in range(2, B + 1):
        if isprime(x):
            F_B.append(x)
    return F_B


def rowEchelonForm(M, n, e):
    row = 0
    col = 0
    rows = len(M)
    cols = len(M[0])

    while row < rows - e and col < cols - 2:
        # Suche Pivot-Element
        t = gcd(n, int64(M[row, col]))
        if t != 1:
            for r in range(row + 1, rows):
                t = gcd(n, int64(M[r, col]))
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
        d = (egcd(int64(M[row, col]), n)[1]) % n
        for i in range(row + 1, rows):
            x = mulmod(int64(-M[i, col]), d, n)
            M[i] = (M[i] + mulmod(M[row], x, n)) % n  # x-Fache der Zeile M[row] wird zur Zeile i addiert
        col += 1
        row += 1
    return True


if __name__ == '__main__':
    print("Ergebnis mit dem Indexkalkül zu 1) p = 1000000007,  g = 5,  h = 956753877: ",
          indexCalculus(5, 956753877, 1000000007))
    print("Ergebnis mit dem Indexkalkül zu 2) p = 1000000000039,  g = 3,  h = 553148792254: ",
          indexCalculus(3, 553148792254, 1000000000039))
    print("Ergebnis mit dem Indexkalkül zu 3) p = 1000000000000037,  g = 2,  h = 531451537204691: ",
          indexCalculus(2, 531451537204691, 1000000000000037))
    print("Ergebnis mit dem Indexkalkül zu 4) p = 1000000000000000003,  g = 2,  h = 849190343074049585: ",
          indexCalculus(2, 849190343074049585, 1000000000000000003))
