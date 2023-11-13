import random
l = 0

am = int(input("Anna arpakuutioiden määrä: "))
for i in range(am):
    ak = random.randint(1,6)
    l += ak
print(l)