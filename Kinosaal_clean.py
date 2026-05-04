

kinosaal = [
    [25, 34, 0, 18, 42],        # Sitzreihe 1
    [0, 0, 51, 60, 33],         # Sitzreihe 2
    [19, 22, 23, 0, 0],         # Sitzreihe 3
    [45, 38, 0, 29, 31]         # Sitzreihe 4
]

def belegte_sitze(belegte_sitze):
    for reihe in kinosaal:
        for sitz in reihe:
            if sitz > 0:
                belegte_sitze += 1
    return belegte_sitze


def durchschnittsalter(alter):
    for reihe in kinosaal:
        for sitz in reihe:
            if sitz > 0:
                alter = alter + sitz
    return alter


def meiste_sitze_in_reihe():
    sitze_pro_reihe = []
    for reihe in kinosaal:
        sitze_in_reihe = 0
        for sitz in reihe:
            if sitz > 0:
                sitze_in_reihe = sitze_in_reihe + 1
        sitze_pro_reihe.append(sitze_in_reihe)

    max_sitze = max(sitze_pro_reihe)

    index_liste = []

    for i in range(0, len(sitze_pro_reihe)):
        if sitze_pro_reihe[i] == max_sitze:
            index_liste.append(i + 1)
    return index_liste


def unter21():
    unter21_liste = []
    for reihe_i, reihe in enumerate(kinosaal):
        for sitz_i, sitz in enumerate(reihe):
            if sitz < 22 and sitz > 0:
                unter21_liste.append(( reihe_i + 1, sitz_i + 1 ))

    return unter21_liste


print(f"Es sind sitze {belegte_sitze(0)} belegt")
print(f"Das durchschnittsalter beträgt: {round(durchschnittsalter(0) / belegte_sitze(0), 2)}.")
print("Die reihe/n mit den meisten Sitzen ist/sind", meiste_sitze_in_reihe())
print("Position von leuten unter 21 (reihe, platz):", unter21())
