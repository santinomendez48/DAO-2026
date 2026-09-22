from envio import Envio
from express import Express
from estandar import Estandar

class Transportadora():

    def __init__(self):
        self.envios = []

    def agregar(self, envio: Envio):
        if not isinstance(envio, Envio):
            raise ValueError("Error solo se pueden agregar envios")
        self.envios.append(envio)

    def importe_total(self):
        return sum(map(lambda x: x.importe(), self.envios))

    def cantidad_envios_prioritarios(self):
        return len(list(filter(lambda x: isinstance(x, Express) and x.urgencia_horas < 4 and x.distancia_km > 50, self.envios)))

    def promedio_importe_estandar(self):
        cant = 0
        acum = 0
        for env in self.envios:
            if isinstance(env, Estandar):
                cant += 1
                acum += env.importe()
        return None if cant == 0 else (acum // cant)

    def cliente_envio_mas_barato(self):
        envio = None
        imp = 0
        for env in self.envios:
            if envio is None or env.importe() < imp:
                envio = env
                imp = env.importe()
        return None if envio is None else envio.cliente
