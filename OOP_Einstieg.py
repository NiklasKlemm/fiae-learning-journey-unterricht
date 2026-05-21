class Wasserfahrzeug:
    knoten = 0
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    def __init__(self, variablen_namen, name, tiefgang, baujahr, besitzer):
        self.variablen_namen = variablen_namen
        self.name = name
        self.tiefgang = tiefgang
        self.baujahr = baujahr
        self.besitzer = besitzer

    def schwimmen(self, knoten):
        self.knoten = knoten

    def segeln(self, segeln):
        self.segeln = segeln

    def ankern(self, ankern):
        self.ankern = ankern

    def ausgabe(self):
        print(f"{self.UNDERLINE}{self.variablen_namen}:{self.RESET}\nName: {self.name} | Tiefgang: {self.tiefgang} | Baujahr: {self.baujahr} | Besitzer: {self.besitzer} | Knoten: {self.knoten}")

wasserfahrzeug1 = Wasserfahrzeug("wasserfahrzeug1","Airwave", 150, 1930, "Maier")
wasserfahrzeug2 = Wasserfahrzeug("wasserfahrzeug2", "Meeresluft", 125, 1980, "Müller")
wasserfahrzeug3 = Wasserfahrzeug("wasserfahrzeug3", "Royal", 115, 2020, "Schulze")

wasserfahrzeug1.schwimmen(15)
wasserfahrzeug2.schwimmen(5)
wasserfahrzeug3.schwimmen(30)

wasserfahrzeug1.ausgabe()
wasserfahrzeug2.ausgabe()
wasserfahrzeug3.ausgabe()


