#from klassen import Kunde
import klassen

'''b1 = klassen.Bestellung("Salami")
print(b1.bestellnummer)
b2 = klassen.Bestellung("Salami")
print(b2.bestellnummer)

b1.pizzaHinzufügen("3", "Funghi", "Mittel", 7.90)
print(b1.aktuelleBestellung[0].name)'''

def main():
    rolle = input("Wie lautet ihre Rolle (Kunde / Mitarbeiter / Lieferan)?")

    if rolle == "Kunde":
        print("Bitte melden Sie sich an")
        #Abfrage der Daten zur Anmeldung / Regestrierung des Kunden über die setter Method da Attribute Privat
        kundeObjekt = klassen.Kunde(kundennummer="1234", id_wert="1")
        kundeObjekt.setName(input("Wie lautet Ihre Name?"))
        kundeObjekt.setStrasse(input("Wie lautet Ihre Straße?"))
        kundeObjekt.setHausnummer(input("Wie lautet Ihre Hausnummer?"))
        kundeObjekt.setPostleitzahl(input("Wie lautet Ihre Postleitzahl?"))
        kundeObjekt.setTelefonnummer(input("Wie lautet Ihre Telefonnummer?"))

        print(f"Wilkommen bei Pizzhut {kundeObjekt.getName()}!")

        #Schleife die Jedes mal Frag ob eine weitere Pizza der Bestellung hinzugefügt werden soll
        bestellungsObjekt = klassen.Bestellung("")
        weitereBestellung = "ja"
        while weitereBestellung == "ja":
            bestaetigung = kundeObjekt.auswahlPizza(bestellungsObjekt)
            
            if bestaetigung == "ja":
                weitereBestellung = input("Möchten Sie eine weitere Pizza Ihrer bestellung hinzufügen?")

        #Bestellung ausgeben und üperprüfen ob Kunde zufrieden
        print("Deine Besttelung sieht wie Folg aus") 

        for pizza in bestellungsObjekt.aktuelleBestellung:
            print(f"1 {pizza.name} Pizza")

        zufrieden = input("Bestellung OK? (ja / nein)")
        if zufrieden == "ja":
            #Bestellung verarbeiten und Zahlung
            gesamtPreis = 0
            for pizza in bestellungsObjekt.aktuelleBestellung:
                gesamtPreis = gesamtPreis + pizza.preis

            print(f"{gesamtPreis}€ macht das dann")
            zahlen = input("Möchten Sie zahlen? (ja / nein)")
            if zahlen == "ja":
                zahlung = klassen.Zahlung(
                                            betrag = gesamtPreis,
                                            zahlungsart = input("Mit Karte oder Bar?"),
                                            )
                zahlung.zahlungAusfuehren()

        else:
            #Abbruch des Programms / der main funktion
            return
    
                


        

        

main()
