import random

hl = random.randint(0, 10)
while True:
    al = int(input("Arvaa luku?: "))
    if al > hl:
        print("Liian suuri arvaus")
    elif al < hl:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break