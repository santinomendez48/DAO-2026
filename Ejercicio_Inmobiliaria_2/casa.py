from inmueble import Inmueble

class Casa(Inmueble):

    def __init__(self, codigo, propietario, superficie, importe_base, dormitorios, pileta: bool):
        super().__init__(codigo, propietario, superficie, importe_base)
        self.dormitorios = dormitorios
        self.pileta = pileta

    def alquiler(self):
        importe_dormitorios = self.dormitorios * 30000
        importe_pileta = 0 if self.pileta is False else 100000
        return self.importe_base + importe_dormitorios + importe_pileta