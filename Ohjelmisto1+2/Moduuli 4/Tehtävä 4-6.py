import random
n = 0

apm = int(input("Anna arvottavien pisteiden määrä: "))
for i in range(apm):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

print("Piin likiarvo on", 4*n/apm)
