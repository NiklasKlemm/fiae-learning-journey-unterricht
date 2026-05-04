lager = [
        [12, 4, 7, 0],
        [3, 15, 0, 9],
        [0, 2, 1, 8]
]


def gesamtanzahl_produkte(anzahl):
    for regal in lager:
        for produkt in regal:
            anzahl = anzahl + produkt

    return anzahl


def regel_mit_meisten_produkten():
    liste = []
    for regal in lager:
        produkte_in_regal = 0
        for produkte in regal:
            produkte_in_regal = produkte_in_regal + produkte

        liste.append(produkte_in_regal)

    meiste_produkte_wert = max(liste)

    index_liste = []

    for i in range(0, len(liste)):
        if liste[i] == meiste_produkte_wert:
            index_liste.append(i + 1)

    return index_liste


def liste_5auf0():
    liste_5auf0 = []
    for regal in lager:
        for produkt in regal:
            if produkt < 6:
                liste_5auf0.append(0)
            else:
                liste_5auf0.append(produkt)

    return liste_5auf0


def positionen_wo_leer():
    index_liste_lager = []
    for regal_i, regal in enumerate(lager):
        for produkt_i, produkt in enumerate(regal):
            if produkt == 0:
                index_liste_lager.append((regal_i + 1, produkt_i + 1))

    return index_liste_lager


print(f"Die Gesamtanzahl aller Produkte beträgte: {gesamtanzahl_produkte(0)}.")
print(f"Das regel mit den meisten Produkten ist {regel_mit_meisten_produkten()}.")
print(f"Liste wo alles unter 5 auf 0 gesetzt wird: {liste_5auf0()}.")
print(f"Positionen wo ein regal leer ist (Reihe, Stelle): {positionen_wo_leer()}.")