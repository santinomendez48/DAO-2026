from gimnasio import Gimnasio
from individual import Individual
from familiar import Familiar

def cargar_membresias(gimnasio: Gimnasio):
    m = open("gimnasio.csv", "r")
    for linea in m:
        campos = linea.split(",")
        tipo = int(campos[0])
        codigo = int(campos[1])
        socio = str(campos[2])
        antiguedad = int(campos[3])
        importe_base = float(campos[4])

        if tipo == 1:
            cant_clases = int(campos[5])
            personal = True if int(campos[6]) == 1 else False
            gimnasio.agregar(Individual(codigo, socio, antiguedad, importe_base, cant_clases, personal))
        elif tipo == 2:
            importe_seguro = float(campos[5])
            integrantes = int(campos[6])
            gimnasio.agregar(Familiar(codigo, socio, antiguedad, importe_base, importe_seguro, integrantes))
        else:
            raise ValueError("El tipo de membresia ingresado no es valido")
    m.close()

def main():
    gimnasio = Gimnasio()
    cargar_membresias(gimnasio)
    print(gimnasio.suma_cuotas())
    print(gimnasio.cantidad_socios_premium())
    print(gimnasio.socio_cuota_mas_baja())

if __name__ == "__main__":
    main()