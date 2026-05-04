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


def body(tag, ankunfszeit, gehenszeit):
    while tag < 31:
        liste_neu = []
        for datensatz in liste:
            if datensatz[0] == tag:

                if ankunfszeit == 0:
                    ankunfszeit = datensatz[1]


                if ankunfszeit != 0 and datensatz [1] != ankunfszeit:
                    gehenszeit = datensatz[1]
                print(tag, ankunfszeit, gehenszeit)
        tag += 1

body(0, 0, 0)

''''#print(tag, f"{liste_neu[0]}\t {liste_neu[1]}\t ")
                liste_neu.append(datensatz[1])
                #print(liste_neu)

                if len(liste_neu) == 1:
                    print(tag, f"{liste_neu[0]}\t \t eine buchung fehlt")

                if len(liste_neu) == 2:
                    print(tag, f"{liste_neu[0]}\t {liste_neu[1]}\t ")

                else:
                    print(tag, f"\t \t nicht anwesend")



        tag += 1'''





'''    zaehler_tage = 2  #1
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
'''


body(0)


def fußzeile():
    print("================================================")
    print("Summe\t Anwesenheit\t") #VARIABLE anwesenheit errechnen)


