#from klassen import Kunde
import klassen

def main():
    rolle = input("Wie lautet ihre Rolle (Kunde / Mitarbeiter / Lieferan)?")
    if rolle == "Kunde":
        print("Bitte melden Sie sich an")
        kundeObjekt = klassen.Kunde(kundennummer="1234", id_wert="1")
        
        kundeObjekt.setName("Hans")
        kundeObjekt.setStrasse(input("Wie lautet Ihre Straße?"))
        kundeObjekt.setHausnummer(input("Wie lautet Ihre Hausnummer?"))
        kundeObjekt.setPostleitzahl(input("Wie lautet Ihre Postleitzahl?"))
        kundeObjekt.setTelefonnummer(input("Wie lautet Ihre Telefonnummer?"))

        print(f"Wilkommen bei Pizzhut {kundeObjekt.getName()}!")
        print("""Bitte Wählen Sie Eine Pizza aus!
                
                Pizza\t\t\tGröße\t\tPreis
                ------------------------------------------------
                Margherita\t\tMittel\t\t6.50 EUR
                Salami\t\t\tMittel\t\t7.50 EUR
                Funghi\t\t\tMittel\t\t7.90 EUR
                Quattro Stagioni\tGroß\t\t9.50 EUR
                Diavola\t\t\tGroß\t\t8.90 EUR
            """)
        
        pizza = input()
        if pizza == "Margherita":
            bestellungObjekt = klassen.Bestellung(
                                    bestellnummer = "1",
                                    pizza = "Margherita"
                                    )                  
            bestellungObjekt.pizzaHinzufügen("Margherita", "Mittel", 6,50)

        if pizza == "Salami":
            bestellungObjekt = klassen.Bestellung(
                                    bestellnummer = "2",
                                    pizza = "Margherita"
                                    )                  
            bestellungObjekt.pizzaHinzufügen("Margherita", "Mittel", 6,50)

        if pizza == "Margherita":
            bestellungObjekt = klassen.Bestellung(
                                    bestellnummer = "3",
                                    pizza = "Margherita"
                                    )                  
            bestellungObjekt.pizzaHinzufügen("Margherita", "Mittel", 6,50)

        if pizza == "Margherita":
            bestellungObjekt = klassen.Bestellung(
                                    bestellnummer = "4",
                                    pizza = "Margherita"
                                    )                  
            bestellungObjekt.pizzaHinzufügen("Margherita", "Mittel", 6,50)

        if pizza == "Margherita":
            bestellungObjekt = klassen.Bestellung(
                                    bestellnummer = "12345",
                                    pizza = "Margherita"
                                    )                  
            bestellungObjekt.pizzaHinzufügen("Margherita", "Mittel", 6,50)

        

        

main()
