punkte = [
        [8, 7, 9, 6],
        [5, 6, 5, 4],
        [9, 9, 10, 8],
        [3, 4, 2, 5]
]

def gesamtanzahl_teilnehmer(punkte_gesamt):
    punkte_teilnehmer_liste = []
    teilnehmer_nr = 0
    for teilnehmer in punkte:
        teilnehmer_nr += 1
        punkte_gesamt = 0
        for punkte_in_liste in teilnehmer:
            punkte_gesamt = punkte_gesamt + punkte_in_liste

        punkte_teilnehmer_liste.append([teilnehmer_nr, punkte_gesamt])

    return punkte_teilnehmer_liste

def teilnehmer_meisten_punkte():
    punkte_teilnehmer_liste = []
    for teilnehmner in punkte:
        punkte_teilnehmer = 0
        for wert in teilnehmner:
            punkte_teilnehmer = punkte_teilnehmer + wert
        punkte_teilnehmer_liste.append(punkte_teilnehmer)

    meisten_punkte = max(punkte_teilnehmer_liste)

    for i in range(0, len(punkte_teilnehmer_liste)):
        if punkte_teilnehmer_liste[i] == meisten_punkte:
            return i + 1

def durchschnitt_kategorie():
    punkte_kategorie_liste = []
    for i in range(0, 4):
        punkte_kategorie = 0
        for teilnehmner in punkte:
            punkte_kategorie = punkte_kategorie + teilnehmner[i]
        punkte_kategorie_liste.append(punkte_kategorie)

    meisten_punkte_kategorie = max(punkte_kategorie_liste)

    for i in range(0, len(punkte_kategorie_liste)):
        if punkte_kategorie_liste[i] == meisten_punkte_kategorie:
            sieger_kategorie = i + 1

    print(f"Die kategorie mit den meisten Punkten ist die {sieger_kategorie}. mit {meisten_punkte_kategorie} punkten.")

def teilnehmer_mehr_als_25_punkte():
    mehr_als_25_punkte_liste = []
    for teilnehmer in punkte:
        teilnehmer_punkte = 0
        for wert in teilnehmer:
            teilnehmer_punkte = teilnehmer_punkte + wert
        if teilnehmer_punkte >= 25:
            mehr_als_25_punkte_liste.append(teilnehmer)

    return mehr_als_25_punkte_liste


print(f"Die Gesamten Punktzahl eines Jeden Teilnehmer sind: {gesamtanzahl_teilnehmer(0)}")
print(f"Der Teilnehmer mit den meisten Punkte ist der {teilnehmer_meisten_punkte()}. Teilnehmer")
durchschnitt_kategorie()
print(f"Teilnehmer mit mehr als 25 punkte: {teilnehmer_mehr_als_25_punkte()}")