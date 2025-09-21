# metodo-Euler

## Descripción del Problema

La ecuación diferencial a resolver es:

\[
\frac{dy}{dt} = y, \quad y(0) = 1
\]

Esta es una ecuación diferencial separable, cuya solución exacta se obtiene mediante el método de separación de variables:

\[y(t) = e^t\]

El objetivo de este repositorio es comparar la solución exacta con una aproximación numérica usando el método de Euler.

## Método de Euler

El método de Euler es un esquema de integración numérica que permite aproximar la solución de una ecuación diferencial de la forma:

\[
y_{n+1} = y_n + h \cdot f(t_n, y_n)
\]

Donde \(h\) es el tamaño del paso y \(f(t, y)\) es la función que define la ecuación diferencial.

## Resultados

El código implementa la solución exacta y la aproximación de Euler para el intervalo \(t \in [0, 1]\) con un paso de \(h = 0.2\). Los resultados se grafican para visualizar la precisión de la aproximación.

## Instrucciones para ejecutar el código

1. Clona el repositorio a tu máquina local.
2. Ejecuta el archivo Python con cualquier entorno que soporte Python 3.x y las librerías `numpy` y `matplotlib`.
3. El código generará una gráfica comparando la solución exacta y la aproximación de Euler.

