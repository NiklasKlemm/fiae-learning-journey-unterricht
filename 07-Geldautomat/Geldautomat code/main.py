from classes import Geldautomat, Kunde

def main(kunde_objekt, geldautomat_objekt):
    karte_eingeben = input("Karte eingeben?")

    if karte_eingeben == "ja":
        kunde_objekt.karte_eingeben(geldautomat_objekt) #Karte eingabe
        geldautomat_objekt.karte_ueberpruefen(kunde_objekt) #Karte üperpüfen

        if kunde_objekt.gueltig == True:
            kunde_objekt.pin_eingeben()   #Pin Abfrage

            if kunde_objekt.authentifizierung_pin == True:

                geldbetrag = kunde_objekt.geldbetrag_eingeben()  #Geldbetrag eingeben
                geldautomat_objekt.aktualisieren_konto(geldbetrag, kunde_objekt) #Aktualisieren Konto
                geldautomat_objekt.karte_ausgeben() #Karte ausgeben
                kunde_objekt.karte_entnehmen() #Karte entnehmen
                geldautomat_objekt.geld_ausgeben(geldbetrag) #Geld ausgabe
                kunde_objekt.geld_entnehmen() #Kunde nimmt Geld

    print("--- VORGANG BEENDET ----")


kunde = Kunde(pin=1234, gueltig=True, kontostand=1000)
geldautomat = Geldautomat()

main(kunde, geldautomat)

'''LEARNINGS: Zu viel Programmlogik in den Klassen-Methoden definiert anstatt in der main.py'''
