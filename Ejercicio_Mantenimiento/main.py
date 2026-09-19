from mantenimiento import Mantenimiento
from preventivo import Preventivo
from correctivo import Correctivo
from maquina import Maquina

def cargarMantenimientos():
    mantenimientos = []
    m = open("data/mantenimientos.csv", "r")
    m.readline()
    for linea in m:
        campos = linea.strip().split(",")
        tipoMantenimiento = int(campos[0])
        fecha = str(campos[1])
        operario = str(campos[2])
        importeRepuesto = float(campos[3])
        if tipoMantenimiento == 1:
            resultadoMantenimiento = int(campos[4])
            importeInsumos = float(campos[5])
            mantenimiento = Preventivo(operario, fecha, importeRepuesto, importeInsumos, resultadoMantenimiento)
        else:
            horasParada = float(campos[4])
            importeTecnico = float(campos[5])
            mantenimiento = Correctivo(operario, fecha, importeRepuesto, horasParada, importeTecnico)
        mantenimientos.append(mantenimiento)
    m.close()
    return mantenimientos

def main():
    print("------------ INICIO DEL SISTEMA ------------")
    maquina = Maquina("Maquina 1")
    print("--------- Maquina: ", maquina.nombre, "---------")
    print("------------ CARGANDO DATOS ------------")
    mantenimientos = cargarMantenimientos()
    for m in mantenimientos:
        maquina.registrarMantenimiento(m)
    print("------------ DATOS CARGADOS CON EXITO ------------")
    print("--------------------------------------------------")
    print("--------- Resultados: ---------")
    sumaGastos = maquina.sumaGastos()
    print("Suma total de gastos en mantenimientos: ", sumaGastos)
    cantMantCaros = maquina.cantidadMantenimientosCaros()
    print("Cantidad de mantenimientos caros: ", cantMantCaros)
    roturaMasLarga = maquina.roturaMasLarga()
    print("Rotura mas larga: ", roturaMasLarga)

if __name__ == "__main__":
    main()
