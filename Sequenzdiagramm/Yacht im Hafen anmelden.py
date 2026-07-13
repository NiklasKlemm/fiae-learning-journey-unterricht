class Mieter:

    def anmeldedaten_eingeben(self):
        benutzername = input("Wie lautet dein Benutzername?")
        passwort = input("Wie lautet dein Passwort?")
        return benutzername, passwort

    def anmeldung_erfolgreich(self):
        print("Loing erfolgreich!")

    def anmeldung_abgelehnt(self):
        print("Loing fehlgeschlagen!")

class MeldeApp:


    def anmeldedaten_uebermitteln(self, benutzername, passwort, datenbank_objekt, mieter_objekt):
        daten_ok = datenbank_objekt.daten_ueberpruefen(benutzername, passwort)

        if daten_ok == True:
            yacht = Yacht()
            mieter_objekt.anmeldung_erfolgreich()

        else:
            mieter_objekt.anmeldung_abgelehnt()

class Datenbank:

    def __init__(self):
        self.daten = {"1": "2",
                      "user2": "password2",
                      "user3": "password3"
                      }

    def daten_ueberpruefen(self, benutzername, passwort):
        if self.daten.get(benutzername) == passwort:            #.get holt sich den Dictionary Eintrag wo die 1. stelle benutername enspricht, anschließend wird passwort an 2. stelle gecheckt
            print("Login erfolgreich")
            return True

        else:
            print("Login Fehlgeschlagen")
            return False

class Yacht:
    pass

mieter = Mieter()
app = MeldeApp()
db = Datenbank()

def main(mieter_objekt, meldeapp_objekt, datenbank_objekt):
    benutzername, passwort = mieter_objekt.anmeldedaten_eingeben()                          #Benutzername und passwort festlegen
    meldeapp_objekt.anmeldedaten_uebermitteln(benutzername, passwort, datenbank_objekt, mieter_objekt)     #meldapp holt sich die login daten und ruft die üperprüfungs methode in Datenbank auf


main(mieter, app, db)