from mantenimiento import Mantenimiento

class Correctivo(Mantenimiento):

    def __init__(self, operario: str, fecha: str, importeRepuestos: float, horasParada: float, importeTecnico: float):
        super().__init__(operario, fecha, importeRepuestos)
        self.horasParada = horasParada
        self.importeTecnico = importeTecnico

    def __str__(self):
        aux = super().__str__()
        aux += f" - Horas Parada: {self.horasParada} - Importe Tecnico: {self.importeTecnico}"
        return aux

    def esPreventivo(self) -> bool:
        return False

    def costoTotal(self) -> float:
        return self.importeRepuestos + self.importeTecnico
