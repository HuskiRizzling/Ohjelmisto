vu = int(input("Anna minulle vuosiluku: "))
if vu % 4 == 0:
    if vu % 400 != 0 and vu % 100 == 0:
        print("Vuosi ei ole karkausvuosi")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi")
