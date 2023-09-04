luvut = []

while True:
    a = input("Anna luku: ")
    if a == "":
        break
    luvut.append(int(a))
luvut.sort()
luvut.reverse()
for i in range(5):
    print(luvut[i])