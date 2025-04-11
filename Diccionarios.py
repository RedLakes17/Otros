#Los diccionarios asignan pares de valores
PobalcionPais={"Mexico":120, "EU":360, "Canada":40, "Brasil":430} #Los keys deben ser objetos inmutables, como por ejemplo aqui lo es el texto
print(PobalcionPais["Canada"])

#Metodos
print(PobalcionPais.keys())

#Anadir mas valors al diccionario
PobalcionPais['Colombia']=60
print(PobalcionPais)
del(PobalcionPais['Canada'])
print(PobalcionPais)

#Para usar un for se debe usar el metodo items para que tome cada key con su valor
for x,y in PobalcionPais.items():
    print("El pais "+str(x)+" tiene "+str(y)+" millones de habitantes")