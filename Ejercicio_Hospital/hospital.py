from atencion import Atencion
from atencion_medica import AtencionMedica
from atencion_farmacia import AtencionFarmacia

class Hospital:

    def __init__(self, razonSocial: str):
        self.razonSocial = razonSocial
        self.atencionesRealizadas = []

    def __str__(self):
        aux = f"Hospital: {self.razonSocial}"
        aux += "\nAtenciones:\n"
        for atencion in self.atencionesRealizadas:
            aux += f"  - {atencion}\n"
        return aux

    def addAtencion(self, atencion: Atencion) -> None:
        self.atencionesRealizadas.append(atencion)

    def importe_total_atencion_consulta(self) -> float:
        total = 0
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica):
                total += atencion.importe
        return total

    def importe_promedio_atenciones(self, importe1: float, importe2: float) -> float:
        total = 0
        count = 0
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica):
                if importe1 < atencion.importeACobrar() < importe2:
                    total += atencion.importeACobrar()
                    count += 1
        if count == 0:
            return 0
        return total / count

    def codigo_primera_atencion_habitual(self) -> int:
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica):
                if atencion.paciente.habitual:
                    return atencion.codigo
        return 0

    def atencionesMedicas(self):
        aux = []
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionMedica):
                aux.append(atencion)
        return aux

    def atencionesFarmacias(self):
        aux = []
        for atencion in self.atencionesRealizadas:
            if isinstance(atencion, AtencionFarmacia):
                aux.append(atencion)
        return aux
