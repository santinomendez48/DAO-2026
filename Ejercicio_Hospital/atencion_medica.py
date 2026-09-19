from atencion import Atencion
from paciente import Paciente

class AtencionMedica(Atencion):

    def __init__(self, codigo: int, tipoDeCobro: int, paciente: Paciente, importe: float):
        super().__init__(codigo = codigo, tipoDeCobro = tipoDeCobro)
        self.paciente = paciente
        self.importe = importe

    def __str__(self):
        aux = super().__str__()
        aux += f" - {self.paciente.__str__()} - Importe a cobrar: {self.importeACobrar():.2f}"
        return aux

    def importeACobrar(self) -> float:
        importe_final = self.importe
        if self.paciente.habitual:
            importe_final *= 0.75  # Descuento del 25% para pacientes habituales
        if self.tipoDeCobro == 2:
            importe_final *= 1.20  # Recargo del 20% para tipo de cobro 2
        else:
            importe_final *= 0.90  # Descuento del 10% para tipo de cobro 1
        return importe_final
    
    def esPacienteHabitual(self):
        return self.paciente.habitual
