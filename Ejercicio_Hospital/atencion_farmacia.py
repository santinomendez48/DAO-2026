from atencion import Atencion

class AtencionFarmacia(Atencion):

    def __init__(self, codigo: int, tipoDeCobro: int, importeTotal: float, descuento: int):
        super().__init__(codigo, tipoDeCobro)
        self.importeTotal = importeTotal
        self.descuento = descuento

    def __str__(self):
        aux = super().__str__()
        aux += f" - Importe a cobrar: {self.importeACobrar():.2f} - Importe Medicamentos: {self.importeTotal} - Descuento: {self.descuento}%"
        return aux

    def importeACobrar(self) -> float:
        importe_final = self.importeTotal
        if self.descuento > 0:
            importe_final -= self.descuento  # Aplicar descuento del cupón
        if self.tipoDeCobro == 2:
            importe_final *= 1.30  # Recargo del 30% para tipo de cobro 2
        else:
            importe_final *= 0.95  # Descuento del 5% para tipo de cobro 1
        return importe_final
