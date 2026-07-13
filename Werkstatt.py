class Lampe:
    def __init__(self, status):
        self.status = status


class Schalter:
    def einschalten(self, lampe_object):
        lampe_object.status = True



    def ausschalten(self, lampe_object):
        lampe_object.status = False


lampe = Lampe(status=False)
schalter = Schalter()
schalter.einschalten(lampe)
print(lampe.status)