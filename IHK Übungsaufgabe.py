#liste = personnr     zeiten             jahr            monat
          #  2        8-17:20uhr          2013             3


liste = [
        [2, 480],
        [2, 1040],
        [3, 470],
        [6, 480],
        [6, 960],
        [7, 990],
        [8, 480],
        [8, 960],
        [30,990]
    ]

def kopfzeile():
    print("Mitarbeiter: 12345           Mai 2013")
    print("Tag\t Kommen\t Gehen\t Anwesenheit\t Bemerkung\t")
    print("================================================")


def body():
    zaehler_tage = 2  #1
    datensatz = 0

    while  zaehler_tage < 31:
        if zaehler_tage == liste[datensatz][0] and zaehler_tage == liste[datensatz + 1][0]:
            print(f"Tag: {liste[datensatz][0]} {liste[datensatz][1] // 60}:{liste[datensatz][1] % 60}")
            print(f"Tag: {liste[datensatz +1][0]} {liste[datensatz +1][1] // 60}:{liste[datensatz+1][1] % 60}")


        elif zaehler_tage == liste[datensatz][0]:
            print(f"Tag: {liste[datensatz][0]} {liste[datensatz][1] // 60}:{liste[datensatz][1] % 60}")


        else:
            print(f"Tag: {zaehler_tage}: Kein Eintrag gefunden.")
        zaehler_tage += 1
        datensatz += 1





    '''for eintrag in liste :
        if zaehler_tage == eintrag[0]: #liste[datensatz][0]:
                print(f"Tag: {eintrag[0]} {eintrag[1] // 60}:{eintrag[1] % 60}")

        else:
            #datensatz += 1

            print(f"Tag: {zaehler_tage}: Kein Eintrag gefunden.")
            zaehler_tage += 1'''


body()


def fußzeile():
    print("================================================")
    print("Summe\t Anwesenheit\t") #VARIABLE anwesenheit errechnen)


