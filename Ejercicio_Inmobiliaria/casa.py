from inmueble import Inmueble

class Casa(Inmueble):

    def __init__(self, codigo: int, propietario: str, superficie: int, alquiler_base: float, dormitorios: int, pileta: bool):
        super().__init__(codigo, propietario, superficie, alquiler_base)
        self.dormitorios = dormitorios
        self.pileta = pileta

    def __str__(self):
        aux = super().__str__()
        return f"{aux} - Dormitorios: {self.dormitorios} - Pilelta: {'Si' if self.pileta else 'No'}"

    def alquiler(self):
        importeFinal = self.alquiler_base
        importeFinal += 30000 * self.dormitorios
        if self.pileta:
            importeFinal += 100000
        return importeFinal
