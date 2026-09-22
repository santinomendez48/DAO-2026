# La aseguradora

## Consigna (tipo parcial)

Una aseguradora administra las pólizas de sus clientes. Puede asegurar **autos** o **hogares**.

De cada póliza se conoce un código numérico, el nombre del asegurado, la antigüedad del cliente en la aseguradora (en años) y el importe base de la prima mensual.

El importe base es fijado por la aseguradora, pero la prima definitiva se calcula a partir del importe base y de las características particulares de cada tipo de póliza.

- En las pólizas de **auto**, si el vehículo tiene menos de 3 años de antigüedad se recarga $80.000 a la prima base (mayor valor a asegurar), y si el vehículo es de **gama alta** se recargan $150.000 adicionales.
- En las pólizas de **hogar**, si la vivienda tiene más de 120 metros cubiertos se recargan $60.000, y si la vivienda posee **alarma monitoreada** se descuentan $40.000.

Se necesita un programa que lea del archivo `aseguradora.csv` la lista de todas las pólizas y las almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Prima total**: informe la suma de las primas de todas las pólizas.
2. **Cantidad de pólizas de riesgo**: informe la cantidad de pólizas de auto cuyo vehículo tenga menos de 3 años, sea de gama alta, **y** cuyo cliente tenga menos de 1 año de antigüedad como cliente de la aseguradora (cliente nuevo con un vehículo caro).
3. **Promedio de primas de hogar**: informe el promedio de las primas de las pólizas de hogar. Si no hay ninguna póliza de hogar cargada, debe devolver `None`.
4. **Asegurado con la prima más alta**: informe el nombre del asegurado cuya prima definitiva sea la más alta, considerando **tanto autos como hogares**. Si no hay pólizas cargadas, debe devolver `None`.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los métodos anteriores.

### Estructura del archivo `aseguradora.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por póliza):

1. Tipo de póliza: 1 para auto y 2 para hogar
2. Código: número sin repetición que identifica cada póliza
3. Nombre del asegurado
4. Antigüedad del cliente: número entero expresado en años
5. Prima base: número de tipo float
6. Si es auto, la antigüedad del vehículo en años; si es hogar, los metros cubiertos
7. Si es auto, un número 1 si es de gama alta y 0 si no; si es hogar, un número 1 si tiene alarma monitoreada y 0 si no

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Poliza(codigo, asegurado, antiguedad_cliente, prima_base)` — clase base con atributos homónimos y método `prima()`.
- `Auto(codigo, asegurado, antiguedad_cliente, prima_base, antiguedad_vehiculo, gama_alta)` — `gama_alta` booleano; redefine `prima()`.
- `Hogar(codigo, asegurado, antiguedad_cliente, prima_base, metros_cubiertos, alarma)` — `alarma` booleano; redefine `prima()`.
- `Aseguradora()` — contiene la colección de pólizas y ofrece:
  - `agregar(poliza)`
  - `prima_total()`
  - `cantidad_polizas_riesgo()`
  - `promedio_primas_hogar()`
  - `asegurado_prima_mas_alta()`

## Archivos

- `aseguradora.csv` — datos de ejemplo.
- `test_aseguradora.py` — casos de prueba (pytest).

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (por ejemplo `auto.py`, `hogar.py`, `aseguradora.py`, y opcionalmente `poliza.py`) junto a `test_aseguradora.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 20 pruebas en verde.
