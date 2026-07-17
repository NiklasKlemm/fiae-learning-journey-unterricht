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

    def auswahlPizza():
        pass

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

    def __init__(self, bestellnummer, pizza):
        self.bestellnummer = bestellnummer
        self.pizzen = pizza
        self.datum = datetime.now()
        self.status = "In Bearbeitung"

    def pizzaGesamtanzahl():
        pass

    def pizzaHinzufügen(self, pizzaid, pizza, groesse, preis):
        pizza = Pizza(pizzaid, pizza, groesse, preis )

    def getStatus():
        pass

    def getKunde():
        pass

    def setStatus():
        pass

    def berechneGesamtpreis():
        pass


class Zahlung:

    def __init__(self, zahlungsid, betrag, zahlungsart, status):
        self.zahlungsid = zahlungsid
        self.betrag = betrag
        self.zahlungsart = zahlungsart
        self.status = status

    def zahlungAusfuehren():
        pass

    def getStatus():
        pass