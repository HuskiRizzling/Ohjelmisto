import random

class Hissi:
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.alinkerros = alin
        self.ylinkerros = ylin

    def ylös(self):
        self.kerros += 1
        print(f'Kerros: {self.kerros}')

    def alas(self):
        self.kerros -= 1
        print(f'Kerros: {self.kerros}')

    def siirry(self, dest):
        while self.kerros < dest and self.kerros < self.ylinkerros:
            self.ylös()
        while self.kerros > dest and self.kerros > self.alinkerros:
            self.alas()

class Talo:
    def __init__(self, alin, ylin, hissit):
        self.hissit = [Hissi(alin, ylin) for _ in range(hissit)]
        self.ylin = ylin
        self.alin = alin

    def aja_hissiä(self, hissinumero, kohdekerros):
        if hissinumero < 1 or hissinumero > len(self.hissit):
            print(f'Hissiä {hissinumero} ei ole.')
            return
        hissi = self.hissit[hissinumero - 1]
        hissi.siirry(kohdekerros)
        if kohdekerros < self.alin:
            kohdekerros = self.alin
        elif kohdekerros > self.ylin:
            kohdekerros = self.ylin
        print(f'Hissi {hissinumero} on nyt kerroksessa {kohdekerros}')


talo = Talo(1, 25, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 17)
for i in range(5):
    talo.aja_hissiä(random.randint(1, 3), random.randint(1, 25))