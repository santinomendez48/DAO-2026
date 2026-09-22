# El gimnasio

## Consigna (tipo parcial)

Un gimnasio de la ciudad administra las membresías de sus socios.

De cada membresía se conoce un código numérico, el nombre del socio, la antigüedad en el gimnasio expresada en años, y el importe base de la cuota mensual.

El importe base es fijado por el gimnasio, pero el importe definitivo de la cuota se calcula a partir del importe base y de las características particulares de cada tipo de membresía.

- En el caso de las membresías **individuales**, al importe base se le adicionan $30.000 por cada clase grupal que el socio tenga incluida en su plan, y $100.000 si el socio cuenta con personal trainer.
- Las membresías **familiares** ven incrementado su importe base en $20.000 si el grupo familiar tiene menos de 4 integrantes, y se les incorpora siempre el importe del seguro contratado.

Se necesita un programa que lea del archivo `gimnasio.csv` la lista de todas las membresías y las almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Suma de cuotas**: informe el total a recaudar en concepto de cuotas si todos los socios están al día.
2. **Cantidad de socios premium**: informe la cantidad de socios con membresía individual que tengan más de 2 años de antigüedad, más de 3 clases grupales incluidas, y que cuenten con personal trainer.
3. **Socio de la cuota más baja**: informe el nombre del socio con membresía familiar cuya cuota definitiva sea la más baja.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `gimnasio.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por membresía):

1. Tipo de membresía: 1 para individual y 2 para familiar
2. Código: número sin repetición que identifica cada membresía
3. Nombre del socio
4. Antigüedad: número entero expresado en años
5. Importe base: número de tipo float
6. Si es individual, la cantidad de clases grupales incluidas; si es familiar, el importe del seguro
7. Si es individual, un número 1 si tiene personal trainer y 0 si no; si es familiar, la cantidad de integrantes del grupo

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Membresia(codigo, socio, antiguedad, importe_base)` — clase base con atributos homónimos y método `cuota()`.
- `Individual(codigo, socio, antiguedad, importe_base, clases_grupales, personal_trainer)` — `personal_trainer` booleano; redefine `cuota()`.
- `Familiar(codigo, socio, antiguedad, importe_base, seguro, integrantes)` — redefine `cuota()`.
- `Gimnasio()` — contiene la colección de membresías y ofrece:
  - `agregar(membresia)`
  - `suma_cuotas()`
  - `cantidad_socios_premium()`
  - `socio_cuota_mas_baja()`

## Archivos

- `gimnasio.csv` — datos de ejemplo.
- `test_gimnasio.py` — casos de prueba (pytest).

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (por ejemplo `individual.py`, `familiar.py`, `gimnasio.py`, y opcionalmente `membresia.py`) junto a `test_gimnasio.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 16 pruebas en verde.
