import random


def heita_noppaa():
    while True:
        sl = random.randint(1, 6)
        print("Saatu silmäluku: ", sl)
        if sl == 6:
            break


heita_noppaa()