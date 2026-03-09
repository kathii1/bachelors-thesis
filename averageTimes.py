import timeit
from statistics import mean

setupBSGS = '''
from babystepGiantstep import bsgs
'''

setupPollardRho = '''
from pollardRho import pollardRho
'''

setupIndexCalculus = '''
from indexCalculus import indexCalculus
'''

setupPohligHellman = '''
from pohligHellman import pohligHellman
'''

if __name__ == '__main__':
    challenges = [(5, 956753877, 1000000007), (3, 553148792254, 1000000000039), (5, 531451537204691, 1000000000000037),
                  (2, 849190343074049585, 1000000000000000003)]
    i = 1
    for c in challenges:
        if i < 4:
            r = 100
            print("Durchschnittliche Zeit, zur Berechnung von ", i, ") mit BSGS: ",
                  mean(timeit.Timer('bsgs(c[0],c[1],c[2])', globals={'c': c}, setup=setupBSGS).repeat(r, 1)))
        else:
            r = 5

        print("Durchschnittliche Zeit, zur Berechnung von ", i, ") mit PollardRho: ",
              mean(timeit.Timer('pollardRho(c[0],c[1],c[2])', globals={'c': c}, setup=setupPollardRho).repeat(r, 1)))
        print("Durchschnittliche Zeit, zur Berechnung von ", i, ") mit Indexkalkül: ",
              mean(timeit.Timer('indexCalculus(c[0],c[1],c[2])', globals={'c': c}, setup=setupIndexCalculus).repeat(r,
                                                                                                                    1)))
        print("Durchschnittliche Zeit, zur Berechnung von ", i, ") mit Pohlig-Hellman: ",
              mean(timeit.Timer('pohligHellman(c[0],c[1],c[2])', globals={'c': c}, setup=setupPohligHellman).repeat(r,
                                                                                                                    1)))
        i += 1
