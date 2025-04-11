''' Un caminante comienza en la posición 0 en una línea recta. Lanza un dado para decidir cómo moverse:

Si el dado muestra 1 o 2, el caminante da un paso hacia atrás (retrocede una posición).
Si el dado muestra 3, 4 o 5, el caminante da un paso hacia adelante (avanza una posición).
Si el dado muestra 6, el caminante lanza el dado nuevamente y suma el resultado al número actual de pasos hacia adelante.
Escribe un programa que:

Realice un número definido de pasos (por ejemplo, 100).
Guarde todas las posiciones del caminante en una lista para poder visualizar su trayectoria.
Use numpy para analizar el desplazamiento final y realizar cálculos adicionales, como la distancia promedio recorrida por varios caminantes si simulas más de uno.'''

import numpy as np
import matplotlib.pyplot as plt

posicionFinal=[]
np.random.seed(123)
paso=0

for u in range(2000):
    posicion=[0]
    for i in range(10000):
        dado=np.random.randint(1,7)
        if dado<=2:
            paso=max(0,dado-1)
        elif dado<=5:
            paso=dado+1
        else:
            paso=paso+np.random.randint(1,7)
        posicion.append(paso)
    posicionFinal.append(posicion[-1])

plt.hist(posicionFinal)
plt.savefig("DistDePosFin200Cami.png")





