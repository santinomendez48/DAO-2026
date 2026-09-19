from abc import ABC, abstractmethod

class Mantenimiento(ABC):

    def __init__(self, operario: str, fecha: str, importeRepuestos: float):
        self.operario = operario
        self.fecha = fecha
        self.importeRepuestos = importeRepuestos

    def __str__(self):
        return f"Operario: {self.operario} - Fecha: {self.fecha} - Importe Total: {self.costoTotal():.2f}- Importe Repuestos: {self.importeRepuestos}"

    @abstractmethod
    def esPreventivo(self) -> bool:
        pass

    @abstractmethod
    def costoTotal(self) -> float:
        pass
