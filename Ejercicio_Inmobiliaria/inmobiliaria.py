from inmueble import Inmueble
from casa import Casa
from departamento import Departamento

class Inmobiliaria:

    def __init__(self):
        self.inmuebles = []
    
    def __str__(self):
        aux = ""
        for inm in self.inmuebles:
            aux += inm.__str__() + "\n"
        return aux

    def agregar(self, inmueble: Inmueble):
        self.inmuebles.append(inmueble)

    def suma_alquileres(self):
        total = 0
        for inm in self.inmuebles:
            total += inm.alquiler()
        return total
    
    def cantidad_casas_premium(self):
        cant = 0
        for inm in self.inmuebles:
            if isinstance(inm, Casa):
                if inm.superficie > 150 and inm.dormitorios > 2 and inm.pileta:
                    cant += 1
        return cant
    
    def propietario_alquiler_mas_bajo(self):
        propietario = ""
        menorAlquiler = float(0)
        for inm in self.inmuebles:
            if isinstance(inm, Departamento):
                if menorAlquiler == 0 or inm.alquiler() < menorAlquiler:
                    menorAlquiler = inm.alquiler()
                    propietario = inm.propietario
        if propietario == "":
            return None
        return propietario
