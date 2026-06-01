# a
from abc import ABC, abstractmethod

class Gehaelter(ABC):
    @abstractmethod
    def berechne_gehalt(self):
        pass


# b
class Festangestellte(Gehaelter):


    def berechne_gehalt(self, stunden):
        self.gehalt = stunden * 50



class Freelancer(Gehaelter):
    def berechne_gehalt(self, stunden):
        self.gehalt = stunden * 100


class Praktikanten(Gehaelter):
    def berechne_gehalt(self, stunden):
        self.gehalt = stunden * 20


def berechnung(mitarbeiter, stunden):
    mitarbeiter.berechne_gehalt(stunden)
    print(mitarbeiter.gehalt)

fa1 = Festangestellte()
fa2 = Festangestellte()
fl1 = Freelancer()
fl2 = Freelancer()
pr1 = Praktikanten()
pr2 = Praktikanten()


mitarbeiter_liste = [fa1, fa2, fl1, fl2, pr1, pr2]
summe_gehalt = 0
for objekt in mitarbeiter_liste:
    objekt.berechne_gehalt(160)
    summe_gehalt = summe_gehalt + objekt.gehalt

print(summe_gehalt)

berechnung(pr1, 160)


