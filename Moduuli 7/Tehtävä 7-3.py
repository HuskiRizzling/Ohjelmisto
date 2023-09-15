lentokentat = {}


while True:
    print("Valitse mitä haluat tehdä:")
    print("Jos haluat lisätä uuden lentoaseman paina (1) + Enter")
    print("Jos haluat hakea jo syötetyn lentoaseman paina (2) + Enter")
    print("Jos haluat lopettaa paina (3) + Enter")

    teht = input("Mitä tehdään? (1,2,3): ")

    if teht == "1":
        ICAO = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentokentat[ICAO] = nimi

    elif teht == "2":
        ICAOi = input("Anna lentoaseman ICAO-koodi: ")
        if ICAOi in lentokentat:
            nimi = lentokentat[ICAO]
            print(f"Lentoaseman {ICAO} nimi on: {nimi}")

    elif teht == "3":
        break

    else:
        print("Virheellinen syöttö")
