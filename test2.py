kinosaal = [
    [25, 34, 0, 18, 42],  # Sitzreihe 1
    [0, 0, 51, 60, 33],  # Sitzreihe 2
    [19, 22, 23, 0, 0],  # Sitzreihe 3
    [45, 38, 0, 29, 31]  # Sitzreihe 4
]


def unter21():
    unter21_liste = []

    # enumerate() gibt uns den Index (reihe_idx) UND den Inhalt der Reihe (reihe)
    for reihe_idx, reihe in enumerate(kinosaal):

        # Noch einmal enumerate() für die einzelnen Sitze in der Reihe
        for sitz_idx, sitz in enumerate(reihe):

            # Überprüfen, ob der Wert zwischen 0 und 21 liegt (Pythonic way)
            if 0 < sitz < 22:
                # Wir speichern die Position als "Tuple" (Reihe, Sitzplatz)
                unter21_liste.append((reihe_idx, sitz_idx))

    print("Positionen der u21 Sitze (Reihen-Index, Sitz-Index):", unter21_liste)


unter21()