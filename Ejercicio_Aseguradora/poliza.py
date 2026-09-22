from abc import ABC, abstractmethod
from validador import Validador

class Poliza(ABC):

    def __init__(self, codigo: int, asegurado: str, antiguedad_cliente: int, prima_base: float):
        self.codigo = Validador.esEnteroPositivo(codigo, "codigo")
        self.asegurado = Validador.esStringNoVacia(asegurado, "asegurado")
        self.antiguedad_cliente = Validador.esEnteroPositivo(antiguedad_cliente, "antiguedad_cliente")
        self.prima_base = Validador.esFloatPositivo(prima_base, "prima_base")

    @abstractmethod
    def prima(self):
        pass
