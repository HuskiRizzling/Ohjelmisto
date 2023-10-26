class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.kuljettumatka = 0

freesiauto = Auto("ABC-123", 142)
print(f"Auton {freesiauto.rekisteritunnus} huippunopeus on {freesiauto.huippunopeus}km/h, sen tämänhetkinen nopeus on {freesiauto.nopeusnyt} ja sen kuljettu matka on {freesiauto.kuljettumatka}.")
