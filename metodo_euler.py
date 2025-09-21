import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
h = 0.2  # paso
t_values = np.arange(0, 1.2, h)  # valores de t en el intervalo [0, 1]
y_exact = np.exp(t_values)  # solución exacta

# Método de Euler
y_euler = np.zeros(len(t_values))
y_euler[0] = 1  # condición inicial

# Aplicamos el método de Euler
for n in range(len(t_values) - 1):
    y_euler[n+1] = y_euler[n] + h * y_euler[n]  # y' = y

# Graficar resultados
plt.plot(t_values, y_exact, label="Solución Exacta", color="blue", linestyle='-', marker='o')
plt.plot(t_values, y_euler, label="Método de Euler", color="red", linestyle='--', marker='x')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Comparación entre la solución exacta y el método de Euler')
plt.legend()
plt.grid(True)
plt.show()
