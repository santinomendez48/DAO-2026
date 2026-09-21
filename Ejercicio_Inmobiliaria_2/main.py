from inmobiliaria import Inmobiliaria
from casa import Casa
from departamento import Departamento

def leer_csv():
    inmuebles = []
    archivo = open("inmuebles.csv")
    for linea in archivo:
        datos = linea.split(",")
        tipo = int(datos[0])
        codigo = int(datos[1])
        propietario = datos[2]
        importe_base = float(datos[3])
        superficie = int(datos[4])

        if tipo == 1:
            dormitorios = int(datos[5])
            pileta = bool(datos[6])
            casa = Casa(codigo, propietario, importe_base, superficie, dormitorios, pileta)
            inmuebles.append(casa)
        elif tipo == 2:
            expensas = float(datos[5])
            piso = int(datos[6])
            departamento = Departamento(codigo, propietario, importe_base, superficie, expensas, piso)
            inmuebles.append(departamento)
        else:
            raise ValueError("El tipo de inmueble es incorrecto: " + tipo)
    archivo.close()
    return inmuebles

def main():
    inmobiliaria = Inmobiliaria()
    inmuebles = leer_csv()
    for inm in inmuebles:
        inmobiliaria.agregar(inm)

    print(inmobiliaria.suma_alquileres())
    print(inmobiliaria.cantidad_casas_premium())
    print(inmobiliaria.propietario_alquiler_mas_bajo())

if __name__ == "__main__":
    main()
