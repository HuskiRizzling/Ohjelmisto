okt = "python"
oss = "rules"
i = 0

while i <= 5:
    i += 1
    kt = input("Anna käyttäjätunnus: ")
    ss = input("Anna salasana: ")
    if kt == okt and ss == oss:
        print("Tervetuloa")
        break
    if i == 5:
        print("Pääsy evätty")
        break
