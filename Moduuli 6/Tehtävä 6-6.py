import math


def pizza(i, n):
    a = (math.pi*(i/2)**2)*10**-4
    return n/a


epk = input("Anna ensimmäisen pizzan halkaisija (cm): ")
eph = input("Anna ensimmäisen pizzan hinta (€): ")
tpk = input("Anna toisen pizzan halkaisija (cm): ")
tph = input("Anna toisen pizzan hinta (€): ")

pitsa = pizza(float(epk), float(eph))
pitsa2 = pizza(float(tpk), float(tph))

if pitsa < pitsa2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    print("Toinen pizza antaa paremman vastineen rahalle")
