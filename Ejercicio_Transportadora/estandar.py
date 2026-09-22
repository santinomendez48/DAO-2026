from envio import Envio
from validador import Validador

class Estandar(Envio):

    def __init__(self, codigo: int, cliente: str, distancia_km: float, importe_base: float, peso: float, fragil: bool):
        super().__init__(codigo, cliente, distancia_km, importe_base)
        self.peso = Validador.esFloatPositivo(peso, "peso")
        self.fragil = Validador.esBooleano(fragil, "fragil")

    def importe(self):
        importe_peso = 0
        if self.peso > 20:
            importe_peso += 5000 * (self.peso - 20)
        importe_fragil = 8000 if self.fragil else 0
        return self.importe_base + importe_peso + importe_fragil
    