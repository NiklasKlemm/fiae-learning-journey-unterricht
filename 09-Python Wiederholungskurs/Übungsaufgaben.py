class Weihnachtsbaum:
    counter = 0
    
    def __init__(self, hoehe, breite):
        self.hoehe = hoehe
        self.breite = breite
        Weihnachtsbaum.counter += 1
        self.id = Weihnachtsbaum.counter
    


baum1 = Weihnachtsbaum(hoehe=input("Höhe?"), breite=input("Breite?"))
baum2 = Weihnachtsbaum(hoehe=input("Höhe?"), breite=input("Breite?"))
baum3 = Weihnachtsbaum(hoehe=input("Höhe?"), breite=input("Breite?"))

liste = [
        baum1,
        baum2,
        baum3
        ]

for objekt in liste:
    print(f"\nBaumnummer: {objekt.id}\nHöhe: {objekt.hoehe}\nBreite: {objekt.breite}")