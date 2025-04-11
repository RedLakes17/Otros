import numpy as np
import matplotlib.pyplot as plt

# Datos para la gráfica
x = np.linspace(0, 10, 100)  # Valores de 0 a 10
y = np.sin(x)  # Función seno

# Crear la figura y los ejes
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Seno", color="b", linewidth=2)

# Personalización
plt.xlabel("X")
plt.ylabel("sin(X)")
plt.title("Gráfica de la función seno")
plt.legend()
plt.grid()

# Mostrar la gráfica
plt.show()
