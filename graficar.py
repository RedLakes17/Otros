#Uso de libreria matplotlib.pyplot
import matplotlib.pyplot as plt

#Creamos listas que podemaos graficar
Decadas=[10,20,30,40,50,60,70,80,90]
Accidentes=[3,4,7,4,6,2,6,9,3]

#Creamos el grafico
plt.plot(Decadas, Accidentes)
plt.xlabel('Decadas')
plt.ylabel('Accidentes ocurridos(en miles)')
plt.title('Miles de accidentes en cdmx en cada decada')
plt.savefig('grafico.png')
plt.clf()

#Creamos grafico scatter
plt.scatter(Decadas, Accidentes)
plt.savefig('graficoScatter.png')
plt.clf()

#Creamos histograma
plt.hist(Accidentes, bins=6)
plt.savefig('graficoHisto.png')
plt.clf()