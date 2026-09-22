from validador import Validador
from poliza import Poliza

class Hogar(Poliza):

    def __init__(self, codigo: int, asegurado: str, antiguedad_cliente: int, prima_base: float, metros_cubiertos: int, alarma: bool):
        super().__init__(codigo, asegurado, antiguedad_cliente, prima_base)
        self.metros_cubiertos = Validador.esEnteroPositivo(metros_cubiertos, "metros_cubiertos")
        self.alarma = Validador.esBooleano(alarma, "alarma")

    def prima(self):
        prima_superficie = 60000 if self.metros_cubiertos > 120 else 0
        prima_alarma = 40000 if self.alarma else 0
        return self.prima_base + prima_superficie - prima_alarma
