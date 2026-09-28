class EisMaschine():

    def __init__(self, name):
        self.name = name
        self.aktuelle_kugeln = None

    def kugeln_auswaehlen(self, kugeln):
        self.aktuelle_kugeln = kugeln

    def produziere(self):
        if self.aktuelle_kugeln:
            print(f"Du entmimmst der {self.name} {self.aktuelle_kugeln} Kugeln Eis")


class Eis_in_waffel():
    def __init__(self, kugeln):
        self.kugeln = kugeln


eismaschine = EisMaschine("Eismaschine")
eis = Eis_in_waffel(3)

eismaschine.kugeln_auswaehlen(eis.kugeln)
eismaschine.produziere()