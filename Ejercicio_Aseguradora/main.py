from aseguradora import Aseguradora
from hogar import Hogar
from auto import Auto

def cargar_datos_csv(aseguradora: Aseguradora):
    m = open("aseguradora.csv","r")
    for linea in m:
        campos = linea.split(",")
        tipo = int(campos[0])
        codigo = int(campos[1])
        nombre = str(campos[2])
        antiguedad_cliente = int(campos[3])
        prima_base = float(campos[4])
        if tipo == 1:
            antiguedad_vehiculo = int(campos[5])
            gama_alta = True if int(campos[6]) == 1 else False
            print(f"gama alta: {gama_alta}")
            aseguradora.agregar(Auto(codigo, nombre, antiguedad_cliente, prima_base, antiguedad_vehiculo, gama_alta))
        elif tipo == 2:
            superficie = int(campos[5])
            alarma = True if int(campos[6]) == 1 else False
            print(f"Alarma: {alarma}")
            aseguradora.agregar(Hogar(codigo, nombre, antiguedad_cliente, prima_base, superficie, alarma))
        else:
            raise ValueError("Error el tipo de poliza ingresado no es el correcto")
    m.close()
    return

def main():
    aseguradora = Aseguradora()
    cargar_datos_csv(aseguradora)
    print(f"Prima Total: {aseguradora.prima_total()}")
    print(f"Cantidad polizas de riesgo: {aseguradora.cantidad_polizas_riesgo()}")
    print(f"Promedio primas hogar: {aseguradora.promedio_primas_hogar()}")
    print(f"Asegurado prima mas alta: {aseguradora.asegurado_prima_mas_alta()}")

if __name__ == "__main__":
    main()
