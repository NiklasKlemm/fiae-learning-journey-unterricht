kinosaal = [
            [25, 34, 0, 18, 42],        #Sitzreihe 1
            [0, 0, 51, 60, 33],         #Sitzreihe 2
            [19, 22, 23, 0, 0],         #Sitzreihe 3
            [45, 38, 0, 29, 31]         #Sitzreihe 4
]


print(kinosaal[0])
belegte_sitze = 0
zeile = -1
spalte = -1


while spalte < len(kinosaal):
    if kinosaal[zeile][spalte] > 0:
        belegte_sitze = belegte_sitze + 1
        spalte = spalte + 1

    else:
        spalte = spalte + 1

print(belegte_sitze)







