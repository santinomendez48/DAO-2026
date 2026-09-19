from inmueble import Inmueble

class Departamento(Inmueble):

    def __init__(self, codigo: int, propietario: str, superficie: int, alquiler_base: float, expensas: float, piso: int):
        super().__init__(codigo, propietario, superficie, alquiler_base)
        self.expensas = expensas
        self.piso = piso

    def __str__(self):
        aux = super().__str__()
        return f"{aux} - Expensas: {self.expensas} - Piso: {self.piso}"

    def alquiler(self):
        importeFinal = self.alquiler_base
        if self.piso < 3:
            importeFinal += 20000
        importeFinal += self.expensas
        return importeFinal
