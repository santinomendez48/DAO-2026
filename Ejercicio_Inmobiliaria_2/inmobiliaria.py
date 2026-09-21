from casa import Casa
from departamento import Departamento

class Inmobiliaria():

    def __init__(self):
        self.inmuebles = []

    def agregar(self, inmueble):
        self.inmuebles.append(inmueble)

    def suma_alquileres(self):
        suma = 0
        for inm in self.inmuebles:
            suma += inm.alquiler()
        return suma

    def cantidad_casas_premium(self):
        cantidad = 0
        for inm in self.inmuebles:
            if isinstance(inm, Casa) and inm.superficie > 150 and inm.dormitorios > 2 and inm.pileta:
                cantidad += 1
        return cantidad

    def propietario_alquiler_mas_bajo(self):
        menor = None

        for inm in self.inmuebles:
            if isinstance(inm, Departamento):
                if menor is None or inm.alquiler() < menor.alquiler():
                    menor = inm
        if menor is None: return None 
        return menor.propietario
    