from mantenimiento import Mantenimiento

resultados = ["funcionando correctamente", "requiere revision", "rotura detectada"]

class Preventivo(Mantenimiento):

    def __init__(self, operario: str, fecha: str, importeRepuestos: float, importeInsumos: float, resultado: int ):
        super().__init__(operario, fecha, importeRepuestos)
        self.importeInsumos = importeInsumos
        if resultado not in [1, 2, 3]:
            raise ValueError("El resultado es invalido")
        self.resultado = resultado
    
    def __str__(self):
        aux = super().__str__()
        aux += f" - Importe Insumos: {self.importeInsumos} - Resultado: {self.resultado}"
        return aux

    def esPreventivo(self) -> bool:
        return True

    def costoTotal(self) -> float:
        return self.importeRepuestos + self.importeInsumos
