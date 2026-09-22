from transportadora import Transportadora
from estandar import Estandar
from express import Express

def cargar_transportadora(transportadora: Transportadora):
    m = open("transportadora.csv", "r")
    for linea in m:
        campos = linea.split(",")
        tipo = int(campos[0])
        codigo = int(campos[1])
        nombre = str(campos[2])
        distancia = float(campos[3])
        importe = float(campos[4])
        if tipo == 1:
            peso = float(campos[5])
            fragil = True if int(campos[6]) == 1 else False
            transportadora.agregar(Estandar(codigo, nombre, distancia, importe, peso, fragil))
        elif tipo == 2:
            urgencia = int(campos[5])
            seguro = float(campos[6])
            transportadora.agregar(Express(codigo, nombre, distancia, importe, urgencia, seguro))
        else:
            raise ValueError("Error el tipo de envio ingresado no es valido")
    m.close()
    return

def main():
    transportadora = Transportadora()
    cargar_transportadora(transportadora)
    print(f"Importe toal: {transportadora.importe_total()}")
    print(f"Cantidad de envios prioritarios: {transportadora.cantidad_envios_prioritarios()}")
    print(f"Promedio de importe de envios estandar: {transportadora.promedio_importe_estandar()}")
    print(f"Cliente del envio mas barato: {transportadora.cliente_envio_mas_barato()}")

if __name__ == "__main__":
    main()
