class Fahrzeug:
    def __init__(self, marke):
        if type(marke) is not str:
            raise Exception("Market must be a string")
        self.marke = marke

class Auto(Fahrzeug):
    def __init__(self, marke):
        super().__init__(marke)


class Motorrad(Fahrzeug):
    def __inti__(self, marke):
        super().__init__(marke)

