from membresia import Membresia
from validadores import Validador

class Familiar(Membresia):

    def __init__(self, codigo: int, socio: str, antiguedad: int, importe_base: float, seguro: float, integrantes: int):
        super().__init__(codigo, socio, antiguedad, importe_base)
        self.seguro = Validador.esFloatPositivo(seguro, "seguro")
        self.integrantes = Validador.esEnteroPositivo(integrantes, "integrantes")

    def __str__(self):
        return super().__str__() + f" {self.seguro} - {self.integrantes} -"

    def cuota(self):
        importe_familiares = 20000 if self.integrantes < 4 else 0
        return self.importe_base + importe_familiares + self.seguro
