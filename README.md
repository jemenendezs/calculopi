# CalculaPi

Proyecto en Python para calcular cifras decimales de π usando algoritmos matemáticos avanzados y de alto rendimiento.

## Descripción

Este repositorio implementa un calculador de π con varios algoritmos rápidos y eficientes, orientados a generar un gran número de cifras decimales con buena precisión. El programa ofrece tres opciones de cálculo:

- Chudnovsky con Binary Splitting
- Gauss-Legendre
- Borwein Cuártico

La aplicación incluye:

- entrada interactiva por consola,
- validación de datos,
- visualización del progreso,
- guardado del resultado en un archivo `.txt`.

## Características

- Calcula decimales de π de forma eficiente.
- Soporta hasta 5,000,000 cifras decimales.
- Implementa múltiples algoritmos matemáticos.
- Muestra una vista previa de las primeras 100 cifras.
- Guarda el resultado en un archivo con nombre dinámico.

## Requisitos

- Python 3.x

## Ejecución

1. Clona este repositorio:

```bash
git clone https://github.com/jemenendezs/calculopi.git
cd calculopi
```

2. Ejecuta el script:

```bash
python calcular_pi.py
```

3. El programa te pedirá:
   - el algoritmo a usar (1, 2 o 3),
   - la cantidad de cifras decimales a calcular.

## Ejemplo de uso

```text
Seleccione el algoritmo rápido a utilizar:
  1. Chudnovsky con Binary Splitting (El más rápido para millones de cifras)
  2. Gauss-Legendre (Muy rápido y preciso)
  3. Borwein Cuártico (Convergencia cuártica ultrarrápida)

Ingrese el número de opción (1, 2 o 3) [Por defecto 1]: 1
Ingrese el número de cifras decimales a calcular (máximo 5,000,000): 100
```

## Algoritmos incluidos

### 1. Chudnovsky con Binary Splitting
Es uno de los métodos más rápidos para calcular π con alta precisión. Está optimizado para grandes cantidades de dígitos.

### 2. Gauss-Legendre
También conocido como Salamin-Brent, usa convergencia cuadrática y es muy eficiente para producir muchas cifras.

### 3. Borwein Cuártico
Un método de convergencia cuártica que es útil para cálculos rápidos y precisos.

## Estructura del proyecto

```text
calculopi/
├── README.md
├── LICENSE
├── calcular_pi.py
└── pi_<n>_cifras.txt  (archivo generado al ejecutar)
```

## Archivos generados

Al ejecutar el programa se genera un archivo con el nombre:

```text
pi_<cantidad>_cifras.txt
```

Este archivo contiene la cadena completa de π calculada.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

Proyecto desarrollado en Python para explorar algoritmos avanzados de cálculo de π.
