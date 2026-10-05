# Laboratorio SOLID - Banco Andino

Ingeniería de Software II - 2026 - Universidad Nacional de Colombia, Sede Bogotá

- **Lenguaje elegido:** Python 3.12
- **Integrantes:** Juan Diego Mendoza Torres, Juliana Parra Caro

## 1. Diagnóstico (Bloque 1)

### 1.1 Tabla de hallazgos


| Clase                           | Letra | Evidencia en el código                                                        | Consecuencia para el banco o el cliente                                      |
| ------------------------------- | ----- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `TransaccionService.transferir` | S     | Valida, calcula comisión, mueve dinero, persiste, imprime, notifica y audita. | Cambiar un SMS o comprobante obliga a tocar la misma clase que mueve dinero. |
| `TransaccionService.transferir` | O     | switch(tipo) conoce MISMO_BANCO, OTRO_BANCO, INTERNACIONAL.                    | Cada nuevo tipo obliga a editar código que ya funcionaba.                   |
| Cuenta / CDT                    | L     | CDT hereda retirar() pero lo rechaza antes del vencimiento.                    | Código que espera que toda Cuenta sea retirable explota con un CDT.         |
| `ProductoBancario`              | I     | Obliga a implementar depósito, retiro, intereses, pago y extracto.            | TarjetaCredito y CreditoVivienda contienen métodos vacíos.                 |
| `TransaccionService`            | D     | Hace new OracleRepositorio() y new SmsGateway().                               | No puede probarse sin conectarse a esas implementaciones.                    |

### 1.2 Experimentos

**Experimento 1**
Para este experiomento se cambia el archivo main.py para que se le cobre mensualmete a Ana, Luis y el cdt de Ana. Salta un error porque un CDT no permite retiros antes de que se venzan.

El error ocurre porque CobroCuotaManejo llama al método retirar() sobre todos los objetos de la lista. Sin embargo, aunque CDT hereda de Cuenta, su implementación de retirar() rechaza la operación mientras no haya llegado la fecha de vencimiento.

En un escenario de producción, si este proceso recorriera un millón de cuentas y la cuenta número 500.000 fuera un CDT, las cuentas anteriores ya habrían sido procesadas, pero la excepción interrumpiría el ciclo y las cuentas restantes no serían cobradas. Esto produciría una ejecución parcial del proceso y un estado inconsistente.

Este comportamiento evidencia un problema en la jerarquía de cuentas, relacionado con el principio de sustitución de Liskov

**Experimento 2**
Se hace un archivo temporal experimento2.py (que se borró antes de enviar el commit), pero es imposible escribir una prueba de una transferencia a `OTRO_BANCO` porque `TransaccionService.__init__` crea internamente `OracleRepositorio` y `SmsTwilio`, así que cualquier prueba abriría una conexión a producción y enviaría un SMS real. No hay parámetro del constructor para reemplazarlos (ni setters).

### 1.3 Medición "antes"


| Métrica                                                  | Antes |
| --------------------------------------------------------- | ----- |
| Líneas del método`transferir`                           | 37    |
| Razones distintas por las que podría cambiar`transferir` | 7     |
| Clases concretas que crea dentro de la clase              | 2     |
| Métodos vacíos o que lanzan "no aplica"                 | 3     |
| ¿Se puede probar`transferir` sin Oracle ni SMS?          | No    |



## 2. Refactorización (Bloque 2)

### Punto de control S

Después de la refactorización, `TransaccionService` coordina la ejecución
de una transferencia delegando las responsabilidades específicas a otros
componentes.

La descripción de su responsabilidad no necesita utilizar la palabra "y",
ya que su función principal es coordinar el proceso.

Si el área legal solicita modificar el formato del comprobante, solo se
debe modificar `comprobante.py`, sin alterar la lógica de
`TransaccionService`.

### Punto de Control O

Habría que modificar main.py para importarlo y usarlo al armar el sistema. Además, se crearía un archivo nuevo para su implementación de TipoTransferencia. transaccion_service.py y los tipos existentes no requieren cambios.

### Punto de Control L

Python no detecta esto al compilar; un verificador estático como mypy o Pyright puede detectar que se pase un CDT al cobro. Eso es mejor porque el error aparece antes de ejecutar y evita que el cobro se interrumpa a mitad del proceso. Para obtener esa detección hay que correr el verificador de tipos.

