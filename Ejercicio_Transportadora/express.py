from envio import Envio
from validador import Validador
class Express(Envio):

    def __init__(self, codigo: int, cliente: str, distancia_km: float, importe_base: float, urgencia_horas: int, seguro_extra: float):
        super().__init__(codigo, cliente, distancia_km, importe_base)
        self.urgencia_horas = Validador.esEnteroPositivo(urgencia_horas, "urgencia_horas")
        self.seguro_extra = Validador.esFloatPositivo(seguro_extra, "seguro_extra")

    def importe(self):
        importe_urgencia = 15000 if self.urgencia_horas < 4 else 0
        return self.importe_base + importe_urgencia + self.seguro_extra
