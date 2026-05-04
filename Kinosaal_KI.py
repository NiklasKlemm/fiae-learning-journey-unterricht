kinosaal = [
    [25, 34, 0, 18, 42],  # Reihe 1 (4 belegt)
    [0, 0, 51, 60, 33],  # Reihe 2 (3 belegt)
    [19, 22, 23, 0, 0],  # Reihe 3 (3 belegt)
    [45, 38, 0, 29, 31]  # Reihe 4 (4 belegt)
]

# 1. Unser Notizzettel (eine leere Liste)
zaehler_pro_reihe = []

# 2. Wir gehen durch jede Reihe und zählen
for reihe in kinosaal:
    belegt = 0
    for sitz in reihe:
        if sitz > 0:
            belegt = belegt + 1

    # Das Ergebnis der Reihe auf den Notizzettel schreiben
    zaehler_pro_reihe.append(belegt)

# Jetzt sieht unser Notizzettel so aus: [4, 3, 3, 4]
print("Belegte Sitze pro Reihe:", zaehler_pro_reihe)

# 3. Den Rekord finden mit den "Superkräften" von Python
rekord_wert = max(zaehler_pro_reihe)  # Findet die größte Zahl (hier: 4)
rekord_reihe = zaehler_pro_reihe.index(rekord_wert) + 1  # Findet die Position

print(f"Die meisten Sitze sind {rekord_wert}. Das ist Reihe {rekord_reihe}.")