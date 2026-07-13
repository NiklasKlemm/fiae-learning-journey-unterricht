class Kunde():

    def __init__(self, pin, gueltig, kontostand):
        self.pin = pin
        self.gueltig = gueltig
        self.authentifizierung_pin = False
        self.kontostand = kontostand


    def karte_eingeben(self, geldautomat):
        Geldautomat.aktive_karte = True


    def pin_eingeben(self):
        pin_eingabe = int(input("Pin?"))
        if pin_eingabe == self.pin:
            self.authentifizierung_pin = True
            print("Pin ist richtig")

        else:
            Geldautomat.karte_einbehalten(self)


    def geldbetrag_eingeben(self):
        geldbetrag = int(input("Wie viel € möchten Sie abheben?"))
        return geldbetrag


    def karte_entnehmen(self):
        print("Kunde entnimmt Karte")


    def geld_entnehmen(self):
        print("Kunde entnimmt Geld")


class Geldautomat():

    def __init__(self):
        self.aktive_karte = None


    def karte_ueberpruefen(self, kunde):
        if kunde.gueltig == True:
            print("Karte ist Gültig")
            return True

        else:
            self.karte_einbehalten()


    def karte_einbehalten(self):
        print("Karte wird einbehalten")


    def aktualisieren_konto(self, geldbetrag, kunde_objekt):
        kunde_objekt.kontostand = kunde_objekt.kontostand - geldbetrag
        print(f"Ihr neuer Kontostand lautet {kunde_objekt.kontostand}€")


    def karte_ausgeben(self):
        self.aktive_karte = False
        print("Karte wird ausgeben")


    def geld_ausgeben(self, geldbetrag):
        print(f"Es werden {geldbetrag}€ ausgeben")
