kinosaal = [
    [25, 34, 0, 18, 42],        # Sitzreihe 1
    [0, 0, 51, 60, 33],         # Sitzreihe 2
    [19, 22, 23, 0, 0],         # Sitzreihe 3
    [45, 38, 0, 29, 31]         # Sitzreihe 4
]

sitze_pro_reihe = []
belegte_sitze = 0
alter = 0
platz_unter21 = []

for reihe in kinosaal:
    sitze_reihe = 0
    for sitz in reihe:

        if sitz < 22 and sitz > 0:
            platz_unter21.append(sitz)
        if sitz > 0:
            alter = alter + sitz
            sitze_reihe = sitze_reihe + 1

            belegte_sitze += 1

    sitze_pro_reihe.append(sitze_reihe)

print("unter 21", platz_unter21)
print("Sitze reihe:", sitze_pro_reihe)

sieger = max(sitze_pro_reihe)

def unter21(platz_unter21, kinosaal):

    unter21_index = []

    for i in range(0 , len(kinosaal)):
        if platz_unter21 == kinosaal[0][3]:
            unter21_index.append("richtig")
            return unter21_index

unter21_index = unter21(platz_unter21, kinosaal)
print("unter21 index", unter21_index)



def reiheSieger(sieger, sitze_pro_reihe):

    laenge = len(sitze_pro_reihe)
    index_liste = []

    for i in range(0,laenge):
        if sitze_pro_reihe[i] == sieger:
            index_liste.append(i+1)
    return index_liste

index_liste = reiheSieger(sieger, sitze_pro_reihe)
print("Die Reihe mit den misten sitzen ist: ", index_liste)

print(f"Es sind {belegte_sitze} Sitze belegt.")
durchschnittsalter = alter / belegte_sitze


print("Durchschnittsalter:", round(durchschnittsalter, 2))

