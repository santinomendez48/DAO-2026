from membresia import Membresia
from validadores import Validador

class Individual(Membresia):

    def __init__(self, codigo: int, socio: str, antiguedad: int, importe_base: float, clases_grupales: int, personal_trainer: bool):
        super().__init__(codigo, socio, antiguedad, importe_base)
        self.clases_grupales = Validador.esEnteroPositivo(clases_grupales, "clases_grupales")
        self.personal_trainer = Validador.esBooleano(personal_trainer, "personal_trainer")

    def __str__(self):
        return super().__str__() + f" {self.clases_grupales} - {self.personal_trainer} -"
    
    def cuota(self):
        importe_clase_grupal = 30000 * self.clases_grupales
        importe_personal_trainer = 100000 if self.personal_trainer else 0
        return self.importe_base + importe_clase_grupal + importe_personal_trainer
