# La transportadora

## Consigna (tipo parcial)

Una empresa de transporte de encomiendas administra los envíos que realiza. Puede tratarse de envíos **estándar** o **express**.

De cada envío se conoce un código numérico, el nombre del cliente, la distancia en kilómetros que debe recorrer y el importe base del servicio.

El importe base es fijado por la empresa, pero el importe definitivo del envío se calcula a partir del importe base y de las características particulares de cada tipo de envío.

- En los envíos **estándar**, si el peso del paquete supera los 20 kilos, se recarga $5.000 por cada kilo que exceda ese límite. Además, si el paquete está marcado como **frágil**, se recarga un importe fijo de $8.000.
- En los envíos **express**, si la entrega debe realizarse en menos de 4 horas, se recarga un importe fijo de $15.000. Además, siempre se incorpora el importe del seguro extra contratado para ese envío.

Se necesita un programa que lea del archivo `transportadora.csv` la lista de todos los envíos y los almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Importe total**: informe la suma de los importes de todos los envíos.
2. **Cantidad de envíos prioritarios**: informe la cantidad de envíos express cuya entrega deba realizarse en menos de 4 horas **y** cuya distancia a recorrer sea mayor a 50 km.
3. **Promedio de importe de envíos estándar**: informe el promedio de los importes de los envíos estándar. Si no hay ningún envío estándar cargado, debe devolver `None`.
4. **Cliente del envío más barato**: informe el nombre del cliente cuyo envío tenga el importe más bajo, considerando **tanto envíos estándar como express**. Si no hay envíos cargados, debe devolver `None`.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los métodos anteriores.

### Estructura del archivo `transportadora.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por envío):

1. Tipo de envío: 1 para estándar y 2 para express
2. Código: número sin repetición que identifica cada envío
3. Nombre del cliente
4. Distancia: número entero expresado en kilómetros
5. Importe base: número de tipo float
6. Si es estándar, el peso del paquete en kilos; si es express, la cantidad de horas en la que debe entregarse
7. Si es estándar, un número 1 si el paquete es frágil y 0 si no; si es express, el importe del seguro extra contratado

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Envio(codigo, cliente, distancia_km, importe_base)` — clase base con atributos homónimos y método `importe()`.
- `Estandar(codigo, cliente, distancia_km, importe_base, peso, fragil)` — `fragil` booleano; redefine `importe()`.
- `Express(codigo, cliente, distancia_km, importe_base, urgencia_horas, seguro_extra)` — redefine `importe()`.
- `Transportadora()` — contiene la colección de envíos y ofrece:
  - `agregar(envio)`
  - `importe_total()`
  - `cantidad_envios_prioritarios()`
  - `promedio_importe_estandar()`
  - `cliente_envio_mas_barato()`

## Archivos

- `transportadora.csv` — datos de ejemplo.
- `test_transportadora.py` — casos de prueba (pytest).

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (por ejemplo `estandar.py`, `express.py`, `transportadora.py`, y opcionalmente `envio.py`) junto a `test_transportadora.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 17 pruebas en verde.
