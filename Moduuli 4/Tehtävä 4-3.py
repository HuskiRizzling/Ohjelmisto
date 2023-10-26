luvut = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luvut.append(int(luku))
print("Pienin luku on:", min(luvut), "\nSuurin luku on:", max(luvut))
