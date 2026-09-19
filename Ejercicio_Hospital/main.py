from hospital import Hospital
from paciente import Paciente
from atencion_medica import AtencionMedica
from atencion_farmacia import AtencionFarmacia

def aBooleano(texto: str) -> bool:
    return texto.strip().lower() == "true"

def cargarPacientes():
    pacientes = {}
    m = open("data/pacientes.csv", "rt")
    m.readline()
    for linea in m:
        campos = linea.strip().split(",")
        codigo_atencion = int(campos[0])
        nombre = campos[1]
        sintoma = int(campos[2])
        habitual = aBooleano(campos[3])
        paciente = Paciente(nombre, sintoma, habitual)
        pacientes[codigo_atencion] = paciente
    m.close()
    return pacientes

def cargarAtencionesMedicas(pacientes):
    atenciones = []
    m = open("data/atenciones_medicas.csv", "rt")
    m.readline()
    for linea in m:
        campos = linea.strip().split(",")
        codigo_atencion = int(campos[0])
        tipo_cobro = int(campos[1])
        importe_consulta = float(campos[2])
        paciente = pacientes[codigo_atencion]
        atencion = AtencionMedica(codigo_atencion, tipo_cobro, paciente, importe_consulta)
        atenciones.append(atencion)
    m.close()
    return atenciones

def cargarAtencionesFarmacia():
    atenciones = []
    m = open("data/atenciones_farmacia.csv", "rt")
    m.readline()
    for linea in m:
        campos = linea.strip().split(",")
        codigo_atencion = int(campos[0])
        tipo_cobro = int(campos[1])
        importe_total = float(campos[2])
        cupon_descuento = float(campos[3])
        atencion = AtencionFarmacia(codigo_atencion, tipo_cobro, importe_total, cupon_descuento)
        atenciones.append(atencion)
    m.close()
    return atenciones

def cargarHospital():
    hospital = Hospital("Hospital Central")
    pacientes = cargarPacientes()
    medicas = cargarAtencionesMedicas(pacientes)
    farmacias = cargarAtencionesFarmacia()
    
    for atencion in medicas:
        hospital.addAtencion(atencion)
        
    for atencion in farmacias:
        hospital.addAtencion(atencion)
        
    return hospital

def main():
    print("--------- INICIO DEL SISTEMA ----------")
    print("--------- Cargando datos ---------")
    
    hospital = cargarHospital()
    
    print("--------- Hospital: ", hospital.razonSocial, "---------")
    print("\n--------- Datos cargados con exito ---------\n")
    
    print("--------- Seleccione la opcion que desee: ---------\n")
    print("1.   Consultar atenciones")
    print("2.   Consultar importe total de atenciones medicas")
    print("3.   Consultar importe promedio de atenciones medicas entre dos importes")
    print("4.   Consultar codigo de la primera atencion medica a un paciente habitual")
    print("5.   Salir\n")
    
    opcion = int(input("Ingrese la opcion: "))
    while opcion != 5:
        if opcion == 1:
            print(hospital.__str__())
        elif opcion == 2:
            print("Importe total de atenciones medicas: ", hospital.importe_total_atencion_consulta())
        elif opcion == 3:
            importe1 = float(input("Ingrese el primer importe: "))
            importe2 = float(input("Ingrese el segundo importe: "))
            if importe1 < importe2:
                print("El importe promedio de atenciones medicas entre los importes ", importe1, " y ", importe2, " es: ", hospital.importe_promedio_atenciones(importe1, importe2))
            else:
                print("Error: El primer importe debe ser menor al segundo importe")
        elif opcion == 4:
            codigo = hospital.codigo_primera_atencion_habitual()
            if codigo != 0:
                print("Codigo de la primera atencion medica a un paciente habitual: ", codigo)
            else:
                print("No se encontro una atencion medica a un paciente habitual")
        else:
            print("Opcion no valida")
        print("\n")
        opcion = int(input("Ingrese la opcion: "))
    print("--------- FIN DEL SISTEMA ----------")

if __name__ == "__main__":
    main()
