from abc import ABC
from abc import abstractmethod

tiposDeCobro = ['efectivo', 'tarjeta de crédito']

class Atencion(ABC):

    def __init__(self, codigo: int, tipoDeCobro: int):
        self.codigo = codigo
        if tipoDeCobro not in [1, 2]:
            raise ValueError("El tipo de cobro ingresado no es válido")
        self.tipoDeCobro = tipoDeCobro

    def __str__(self):
        return f"Atencion Medica {self.codigo} - Tipo de Cobro: {tiposDeCobro[self.tipoDeCobro - 1]}"

    @abstractmethod
    def importeACobrar(self) -> float:
        pass
