from membresia import Membresia
from individual import Individual
from familiar import Familiar

class Gimnasio():

    def __init__(self):
        self.membresias = []

    def __str__(self):
        aux = ""
        for m in self.membresias:
            aux += f"\n {m}"
        return aux

    def agregar(self, membresia: Membresia):
        if not isinstance(membresia, Membresia):
            raise ValueError("Error solo se pueden agregar membresias al gimnasio")
        self.membresias.append(membresia)

    def suma_cuotas(self):
        return sum(list(map(lambda x: x.cuota(), self.membresias)))

    def cantidad_socios_premium(self):
        return len(list(filter(lambda x: isinstance(x, Individual) and x.antiguedad > 2 and 
                               x.clases_grupales > 3 and x.personal_trainer, self.membresias)))

    def socio_cuota_mas_baja(self):
        membresia = None
        cuota = 0
        for memb in self.membresias:
            if isinstance(memb, Familiar):
                if membresia is None or memb.cuota() < cuota:
                    membresia = memb
                    cuota = memb.cuota()
        return membresia.socio if membresia else None
