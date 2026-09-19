from inmobiliaria import Inmobiliaria
from casa import Casa
from departamento import Departamento

def cargar_inmuebles():
    inmuebles = []
    m = open("data/inmuebles.csv", "r")
    for linea in m:
        campos = linea.strip().split(",")
        tipo = int(campos[0])
        codigo = int(campos[1])
        propietario = campos[2]
        alquiler_base = float(campos[3])
        superficie = int(campos[4])
        if tipo == 1:
            dormitorios = int(campos[5])
            pileta = True if campos[6] == "1" else False
            inmuebles.append(Casa(codigo, propietario, superficie, alquiler_base, dormitorios, pileta))
        else:
            expensas = float(campos[5])
            piso = int(campos[6])
            inmuebles.append(Departamento(codigo, propietario, superficie, alquiler_base, expensas, piso))
    return inmuebles

def main():
    print("\n--- Ejercicio Inmobiliaria ---\n")
    inmobiliaria = Inmobiliaria()
    inmuebles = cargar_inmuebles()
    for inm in inmuebles:
        inmobiliaria.agregar(inm)
    print(f"Suma de alquileres: {inmobiliaria.suma_alquileres()}")
    print(f"Cantidad de casas premium: {inmobiliaria.cantidad_casas_premium()}")
    print(f"Propietario del alquiler más bajo: {inmobiliaria.propietario_alquiler_mas_bajo()}")

if __name__ == "__main__":
    main()
