from abc import ABC, abstractmethod
from validadores import Validador
class Membresia(ABC):

    def __init__(self, codigo: int, socio: str, antiguedad: int, importe_base: float):
        self.codigo =  Validador.esEntero(codigo, "codigo")
        self.socio = Validador.esStringNoVacia(socio, "socio")
        self.antiguedad = Validador.esEnteroPositivo(antiguedad, "antiguedad")
        self.importe_base = Validador.esFloatPositivo(importe_base, "importe_base")

    def __str__(self):
        return f"{self.codigo} - {self.socio} - {self.antiguedad} - {self.importe_base} -"

    @abstractmethod
    def cuota(self):
        pass
