''' a) Implementieren Sie eine Basisklasse „Tier“ mit einer Methode „mache_geraeusch()“.
    b) Leiten Sie mehrere Tierklassen (z.B. Hund, Katze, Papagei) ab und überschreiben Sie die Methode entsprechend.
    c) Erstellen Sie eine Funktion „zoo_show(tiere)“, die für alle übergebenen Tiere das jeweilige Geräusch ausgibt.
    d) Erweitern Sie das System um ein weiteres Tier, ohne die bestehende Show-Funktion zu verändern.       '''

#a)
class Tier:
    def mache_gerausch(self):
        pass

#b)
class Hund(Tier):
    def mache_gerausch(self):
        print("Woof")

class Katze(Tier):
    def mache_gerausch(self):
        print("Meow")

class Schaf(Tier):
    def mache_gerausch(self):
        print("Määäh")

#c)
def zoo_show(tier):
    tier.mache_gerausch()

zoo_show(Hund())
zoo_show(Katze())
zoo_show(Schaf())

#d)
class Vogel(Tier):
    def mache_gerausch(self):
        print("Zwischern")

zoo_show(Vogel())