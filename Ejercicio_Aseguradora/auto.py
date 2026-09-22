from validador import Validador
from poliza import Poliza

class Auto(Poliza):

    def __init__(self, codigo: int, asegurado: str, antiguedad_cliente: int, prima_base: float, antiguedad_vehiculo: int, gama_alta: bool):
        super().__init__(codigo, asegurado, antiguedad_cliente, prima_base)
        self.antiguedad_vehiculo = Validador.esEnteroPositivo(antiguedad_vehiculo, "antiguedad_vehiculo")
        self.gama_alta = Validador.esBooleano(gama_alta, "gama_alta")

    def prima(self) -> float:
        prima_antiguedad = 80000 if self.antiguedad_vehiculo < 3 else 0
        prima_gama_alta = 150000 if self.gama_alta else 0
        return self.prima_base + prima_antiguedad + prima_gama_alta
