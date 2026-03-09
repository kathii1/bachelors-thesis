from egcd import egcd
from numpy import zeros, prod
from sympy import factorint

from auxiliaryFunctions import mulmod, modpot
from indexCalculusPH import indexCalculus
from pollardRhoPH import pollardRho


# Berechnet x in h = g^x mod n
def pohligHellman(g, a, p):
    N = p - 1
    pfz = factorint(N)

    # Berechnen der diskreten Logarithmen von kleinerer Gruppenordnung
    i = 0
    x = zeros(shape=len(pfz), dtype='int64')
    n = zeros(shape=len(pfz), dtype='int64')
    m = zeros(shape=len(pfz), dtype='int64')
    for q in pfz:
        if q < 10 ** 4:
            n[i] = q ** pfz[q]  # Ordnung von G_i
            m[i] = N // n[i]
            c = modpot(g, m[i], p)  # g_i
            h = modpot(a, m[i], p)  # a_i
            if n[i] <= 10:
                for y in range(n[i]):
                    if modpot(c, y, p) == h:
                        x[i] = y
                        break
            else:
                x[i] = pollardRho(c, h, p, n[i])
            i += 1
        else:
            break

    # Lösen des diskreten Logarithmus-Problems von großer Gruppenordnung
    if (i < len(x)):
        m[i] = (prod(n[0:i]))
        n[i] = N / m[i]
        c = modpot(g, m[i], p)  # g_i
        h = modpot(a, m[i], p)  # a_i
        x[i] = indexCalculus(c, h, p, n[i])
    return chineseRemainder(n[0:i + 1], m[0:i + 1], x[0:i + 1], N)


def chineseRemainder(n, m, x, N):
    y = zeros(shape=len(n), dtype='int64')
    for i in range(len(n)):
        y[i] = egcd(n[i], m[i])[2]
    x = sum([mulmod(x[i], mulmod(y[i], m[i], N), N) for i in range(len(x))]) % N
    return x


if __name__ == '__main__':
    print("Ergebnis mit Pohlig-Hellman zu 1) p = 1000000007,  g = 5,  a = 956753877: ",
          pohligHellman(5, 956753877, 1000000007))
    print("Ergebnis mit Pohlig-Hellman zu 2) p = 1000000000039,  g = 3,  a = 553148792254: ",
          pohligHellman(3, 553148792254, 1000000000039))
    print("Ergebnis mit Pohlig-Hellman zu 3) p = 1000000000000037,  g = 2,  a = 531451537204691: ",
          pohligHellman(2, 531451537204691, 1000000000000037))
    print("Ergebnis mit Pohlig-Hellman zu 4) p = 1000000000000000003,  g = 2,  a = 849190343074049585: ",
          pohligHellman(2, 849190343074049585, 1000000000000000003))
