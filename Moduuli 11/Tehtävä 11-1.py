class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi,  kirjailija, sivut):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivut = sivut

    def print(self):
        print(f'Kirjan nimi: {self.nimi}\nKirjailija: {self.kirjailija}\nSivumäärä: {self.sivut}\n')


class Lehti(Julkaisu):
    def __init__(self, nimi, julkaisija):
        super().__init__(nimi)
        self.julkaisija = julkaisija

    def print(self):
        print(f'Lehden nimi: {self.nimi}\nPäätoimittaja: {self.julkaisija}\n')


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
aku_ankka.print()
hytti_no_6.print()
