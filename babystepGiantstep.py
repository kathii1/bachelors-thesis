from math import ceil, sqrt


# Berechnet x in h = g^x mod n
def bsgs(g, a, p):
    n = p - 1
    m = ceil(sqrt(n))
    B = dict()  # Babysteps
    for r in range(m):
        B[(a * pow(g, -r, p)) % p] = r

    if 1 in B:  # Prüfe, ob ein Paar (1,r) existiert
        return B[1]

    # Giantsteps
    d = pow(g, m, p)
    q = 1
    c = d
    while True:
        if c in B:
            return q * m + B[c]  # x = qm +r
        c = c * d % p
        q = q + 1


# Challenges
if __name__ == '__main__':
    print("Ergebnis mit Babysteps-Giantsteps zu 1) p = 1000000007,  g = 5,  a = 956753877: ",
          bsgs(5, 956753877, 1000000007))
    print("Ergebnis mit Babysteps-Giantsteps zu 2) p = 1000000000039,  g = 3,  a = 553148792254: ",
          bsgs(3, 553148792254, 1000000000039))
    print("Ergebnis mit Babysteps-Giantsteps zu 3) p = 1000000000000037,  g = 2,  a = 531451537204691: ",
          bsgs(2, 531451537204691, 1000000000000037))
    print("Ergebnis mit Babysteps-Giantsteps zu 4) p = 1000000000000000003,  g = 2,  a = 849190343074049585: ",
          bsgs(2, 849190343074049585, 1000000000000000003))
