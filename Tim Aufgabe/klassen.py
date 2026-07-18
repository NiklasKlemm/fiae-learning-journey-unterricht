from datetime import datetime

class Person():
    
    def __init__(self, id_wert):
        self.__name = ""
        self.__strasse = ""
        self.__hausnummer = ""
        self.__postleitzahl = ""
        self.__telefonnummer = ""
        self.id_wert = id_wert

    def getName(self):
        return self.__name

    def setName(self, neuerName):
        self.__name = neuerName

    def getStrasse(self):
        return self.strasse

    def setStrasse(self, strasse):
        self.strasse = strasse

    def getHausnummer(self):
        return self.hausnummer

    def setHausnummer(self, hausnummer):
        self.hausnummer = hausnummer

    def getPostleitzahl(self):
        return self.postleitzahl

    def setPostleitzahl(self, postleitzahl):
        self.postleitzahl = postleitzahl

    def getTelefonnummer(self):
        return self.telefonnummer

    def setTelefonnummer(self, telefonnummer):
        self.telefonnummer = telefonnummer

    def getid(self):
        return self.id_wert

class Kunde(Person):

    def __init__(self, id_wert, kundennummer):
        super().__init__(  id_wert)
        self.kundennummer = kundennummer

    def auswahlPizza(self, bestellungObjekt):
        #Darstellung der Auswahl + Auswahl durch Input. Anschließend übergabe der Bestellung an "pizzaHinzufügen"
        #Return ausßerdem die Antort aus "pizzaHinzufügen" zwecks weitere Bestellung an die Main
        print("""Bitte Wählen Sie Eine Pizza aus!
                
                Pizza\t\t\tGröße\t\tPreis
                ------------------------------------------------
                Margherita\t\tMittel\t\t6.50 EUR
                Salami\t\t\tMittel\t\t7.50 EUR
                Funghi\t\t\tMittel\t\t7.90 EUR
                Quattro Stagioni\tGroß\t\t9.50 EUR
                Diavola\t\t\tGroß\t\t8.90 EUR
            """)
        
        pizza = input("Welche Pizza darf es sein?")
        if pizza == "Margherita":
            '''bestellungObjekt = Bestellung(
                                    #pizzaid = "1",
                                    pizza = "Margherita"
                                    )    '''              
            return bestellungObjekt.pizzaHinzufügen("1", "Margherita", "Mittel", 6.50)

        elif pizza == "Salami": 
            #bestellungObjekt.pizza = "Salami"              
            return bestellungObjekt.pizzaHinzufügen("2", "Salami", "Mittel", 7.50)

        elif pizza == "Funghi":
            '''bestellungObjekt = Bestellung(
                                    #pizzaid = "3",
                                    pizza = "Funghi"
                                    )      '''            
            return bestellungObjekt.pizzaHinzufügen("3", "Funghi", "Mittel", 7.90)

        elif pizza == "Quattro":
            '''bestellungObjekt = Bestellung(
                                    #pizzaid = "4",
                                    pizza = "Quattro"
                                    )    '''              
            return bestellungObjekt.pizzaHinzufügen("4", "Quattro", "Groß", 9.50)

        elif pizza == "Diavola":
            '''bestellungObjekt = Bestellung(
                                    #pizzaid = "12345",
                                    pizza = "Diavola"
                                    )   '''               
            return bestellungObjekt.pizzaHinzufügen("5", "Diavola", "Groß", 8.90)
        
        else:
            print("Diese Pizza gibt es leider nicht?")

    def bestellungAufgeben():
        pass

    def zahlungDurchführen():
        pass

    def bestellstatusEinsehen():
        pass

    def bewerten():
        pass

class Mitarbeiter:

    def __init__(self, mitarbeiternummer):
        self.mitarbeiternummer = mitarbeiternummer

    def bestellungBestätigen():
        pass

    def bestellungZuweisen():
        pass

    def setBestellstatus():
        pass


class Lieferant:

    def __init__(self, fahrzeugKlasse, standort):
        self.fahrzeugKlasse = fahrzeugKlasse
        self.standort = standort

    def lieferadresseAnzeigen():
        pass

    def setBestellstatus():
        pass


class Pizza:

    def __init__(self, pizzaid, name, groesse, preis):
        self.pizzaid = pizzaid
        self.name = name
        self.groesse = groesse
        self.preis = preis

    def getName():
        pass

    def get_preis():
        pass


class Bestellung:
    bestellnummer = 0

    def __init__(self, pizza):
        Bestellung.bestellnummer += 1
        self.bestellnummer = Bestellung.bestellnummer
        self.pizzen = pizza
        self.datum = datetime.now()
        self.status = "In Bearbeitung"
        self.aktuelleBestellung = []

    def pizzaGesamtanzahl():
        #for pizza in liste
        pass

    def pizzaHinzufügen(self, pizzaid, pizza, groesse, preis):
        #Eintragung der Auswahl in eine Aktuelle Bestellungsliste und return des Inputs ob eine Weiter Bestellung gewünscht ist
        self.aktuelleBestellung.append(Pizza(pizzaid, pizza, groesse, preis))
        return input(f"Möchten Sie 1 {pizza} Ihrer Bestellung hinzufügen?")

    def getStatus():
        pass

    def getKunde():
        pass

    def setStatus():
        pass

    def berechneGesamtpreis():
        pass


class Zahlung:
    zahlungsid = 0
    def __init__(self,  betrag, zahlungsart):
        Zahlung.zahlungsid += 1
        self.betrag = betrag
        self.zahlungsart = zahlungsart
        self.status = "ongoing"

    def zahlungAusfuehren(self):
        print(f"Sie zahlen {self.betrag}€ mit {self.zahlungsart}")

    def getStatus():
        pass