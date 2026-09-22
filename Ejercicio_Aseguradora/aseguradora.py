from poliza import Poliza
from auto import Auto
from hogar import Hogar

class Aseguradora():

    def __init__(self):
        self.polizas = []

    def agregar(self, poliza: Poliza):
        if not isinstance(poliza, Poliza):
            raise ValueError("Error solo se pueden agregar polizas")
        self.polizas.append(poliza)

    def prima_total(self) -> float:
        return sum(map(lambda x: x.prima(), self.polizas))

    def cantidad_polizas_riesgo(self):
        return len(list(filter(lambda x: isinstance(x, Auto) and x.antiguedad_vehiculo < 3 and x.gama_alta and x.antiguedad_cliente < 1, self.polizas)))

    def promedio_primas_hogar(self):
        count = 0
        acum = 0
        for pol in self.polizas:
            if isinstance(pol, Hogar):
                count += 1
                acum += pol.prima()
        if count == 0:
            return None
        return acum // count

    def asegurado_prima_mas_alta(self):
        poliza = None
        prima = 0
        for pol in self.polizas:
            if poliza is None or pol.prima() > prima:
                poliza = pol
                prima = pol.prima()
        return None if poliza is None else poliza.asegurado
        