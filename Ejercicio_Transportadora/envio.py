from abc import ABC, abstractmethod
from validador import Validador

class Envio(ABC):

    def __init__(self, codigo: int, cliente: str, distancia_km: float, importe_base: float):
        self.codigo = Validador.esEnteroPositivo(codigo, "codigo")
        self.cliente = Validador.esStringNoVacia(cliente, "cliente")
        self.distancia_km = Validador.esFloatPositivo(distancia_km, "distancia_km")
        self.importe_base = Validador.esFloatPositivo(importe_base, "importe_base")

    @abstractmethod
    def importe(self):
        pass
