from mantenimiento import Mantenimiento
from correctivo import Correctivo

class Maquina:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mantenimientos = []
    
    def __str__(self):
        return f"Maquina: {self.nombre} - Mantenimientos: {self.mantenimientos}"

    def registrarMantenimiento(self, mantenimiento: Mantenimiento):
        self.mantenimientos.append(mantenimiento)

    def sumaGastos(self) -> float:
        sumaTotal = 0
        for m in self.mantenimientos:
            sumaTotal += m.costoTotal()
        return sumaTotal
    
    def cantidadMantenimientosCaros(self) -> int:
        cantidad = 0
        for m in self.mantenimientos:
            if m.costoTotal() > 10000:
                cantidad += 1
        return cantidad

    def roturaMasLarga(self) -> str:
        duracion = 0
        operario = ""
        fecha = ""
        for m in self.mantenimientos:
            if isinstance(m, Correctivo):
                if m.horasParada > duracion:
                    duracion = m.horasParada
                    operario = m.operario
                    fecha = m.fecha
        if duracion == 0:
            return "No se registraron mantenimientos correctivos"
        return f"Operario: {operario} - Fecha: {fecha} - Duracion: {duracion}"
    