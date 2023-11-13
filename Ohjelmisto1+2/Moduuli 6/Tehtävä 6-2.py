import random


def heita_noppaa(i):
    while True:
        sl = random.randint(1, i)
        print("Saatu silmäluku: ", sl)
        if sl == i:
            break


tahkot = int(input("Anna maksimisilmäluku: "))
heita_noppaa(tahkot)
