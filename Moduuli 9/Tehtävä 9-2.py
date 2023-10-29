class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.kuljettumatka = 0
    def kiihdytä(self, nopeudenmuutos):
        self.nopeusnyt += nopeudenmuutos
        if (self.nopeusnyt > self.huippunopeus):
            self.nopeusnyt = self.huippunopeus
        elif (self.nopeusnyt < 0):
            self.nopeusnyt = 0


freesiauto = Auto("ABC-123", 142)
freesiauto.kiihdytä(30)
freesiauto.kiihdytä(70)
freesiauto.kiihdytä(50)
print(f'{freesiauto.nopeusnyt}')
freesiauto.kiihdytä(-200)
print(f'{freesiauto.nopeusnyt}')