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


h = Hissi(1, 25)
h.siirry(7)
h.siirry(-1)