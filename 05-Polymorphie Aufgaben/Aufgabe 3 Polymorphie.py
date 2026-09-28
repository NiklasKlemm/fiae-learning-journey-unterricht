''' a) Definieren Sie eine gemeinsame Schnittstelle oder abstrakte Basisklasse mit der Methode „berechne_gehalt()“.
    b) Implementieren Sie mindestens drei konkrete Klassen mit jeweils eigener Berechnungslogik.
    c) Schreiben Sie eine Auswertungsfunktion, die für eine Liste von Mitarbeitenden das Gesamtgehalt berechnet.
    d) Reflektieren Sie, welche Vorteile die polymorphe Struktur gegenüber einer if-elif-Konstruktion bietet.'''

#a)
from abc import ABC, abstractmethod

class Gehaelter(ABC):
    @abstractmethod
    def berechne_gehalt(self):
        pass

#b)
class Festangestellte(Gehaelter):
    def __init__(self, stunden):
        self.stunden = stunden

    def berechne_gehalt(self):
        self.gehalt = self.stunden * 50


class Freelancer(Gehaelter):
    def __init__(self, stunden):
        self.stunden = stunden

    def berechne_gehalt(self):
        self.gehalt = self.stunden * 100


class Praktikanten(Gehaelter):
    def __init__(self, stunden):
        self.stunden = stunden

    def berechne_gehalt(self):
        self.gehalt = self.stunden * 20


#c)
mitarbeiter_liste = [Festangestellte(160), Festangestellte(140), Freelancer(60), Freelancer(40), Praktikanten(40), Praktikanten(20)]

def summe_der_gehaelter(liste):
    summe_gehalt = 0
    for objekt in liste:
        objekt.berechne_gehalt()
        summe_gehalt = summe_gehalt + objekt.gehalt
    return summe_gehalt

print(summe_der_gehaelter(mitarbeiter_liste))







'''class Festangestellte(Gehaelter):
    def berechne_gehalt(self, stunden):
        self.gehalt = stunden * 50



class Freelancer(Gehaelter):
    def berechne_gehalt(self, stunden):
        self.gehalt = stunden * 100


class Praktikanten(Gehaelter):
    def berechne_gehalt(self, stunden):
        self.gehalt = stunden * 20

fa1 = Festangestellte()
fa2 = Festangestellte()
fl1 = Freelancer()
fl2 = Freelancer()
pr1 = Praktikanten()
pr2 = Praktikanten()


mitarbeiter_liste = [fa1, fa2, fl1, fl2, pr1, pr2]

def summe_der_gehaelter(liste):

    summe_gehalt = 0
    for objekt in liste:
        objekt.berechne_gehalt(160)
        summe_gehalt = summe_gehalt + objekt.gehalt
    return summe_gehalt

print(summe_der_gehaelter(mitarbeiter_liste))

#=========================================================================='''
