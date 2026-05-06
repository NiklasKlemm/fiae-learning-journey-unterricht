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
    print("Tag\t Kommen\t Gehen\t Anwesenheit\tBemerkung\t")
    print("========================================================")


def body(tag, anwesenheit):
    while tag < 31:
        liste_neu = []
        for datensatz in liste:
            if datensatz[0] == tag:
                liste_neu.append(datensatz[1])

        if len(liste_neu) == 0:
            print(f"{tag}\t \t \t \t \t 00:00\t \t \tnicht anwesend")

        if len(liste_neu) == 1:
            print(f"{tag}\t {liste_neu[0] // 60:02d}:{liste_neu[0] % 60:02d}\t \t \t 00:00\t \t \teine Buchung fehlt")

        if len(liste_neu) == 2:
            anwesenheit = anwesenheit + (liste_neu[1] - liste_neu[0])
            print(f"{tag}\t {liste_neu[0] // 60:02d}:{liste_neu[0] % 60:02d}\t {liste_neu[1] // 60}:{liste_neu[1] % 60:02d}\t {(liste_neu[1] - liste_neu[0]) // 60:02d}:{(liste_neu[1] - liste_neu[0]) % 60:02d}")

        tag += 1
    return anwesenheit


def fußzeile():
    print("========================================================")
    print(f"Summe Anwesenheit:\t {anwesenheit // 60}:{anwesenheit % 60:02d} ") #VARIABLE anwesenheit errechnen)


kopfzeile()
anwesenheit = body(1, 0)
fußzeile()

#scrapped ideen für den body
''''
print(tag, f"{liste_neu[0]}\t {liste_neu[1]}\t ")
    liste_neu.append(datensatz[1])
    print(liste_neu)

        if len(liste_neu) == 1:
            print(tag, f"{liste_neu[0]}\t \t eine buchung fehlt")

        if len(liste_neu) == 2:
            print(tag, f"{liste_neu[0]}\t {liste_neu[1]}\t ")

        else:
            print(tag, f"\t \t nicht anwesend")

        tag += 1

=========

zaehler_tage = 1  
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
        
=====
        
        if ankunfszeit == 0:
            ankunfszeit = datensatz[1]

        if ankunfszeit != 0 and datensatz [1] != ankunfszeit:
            gehenszeit = datensatz[1]
            print(tag, ankunfszeit, gehenszeit)
'''