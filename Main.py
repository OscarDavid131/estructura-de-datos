#Listas enlazadas
from struct import pack_into

lista5 = [0,1,2,3]
lista6 = ["A","B","C"]
lista7 = [lista5,lista6]
print(lista7)
print(lista7[0])#Muestra solo lista 5
print(lista7[1])#Muestra solo lista 6
print(lista7[1][0])#Muestra de la lista6 el elemento en el indice 0

#Operaciones con listas
#CONCATENACION
lista8 = ["A","B","C","D","E"]
lista9 = [1,2,3,4,5]
lista10 = lista8 + lista9
print(lista10)
print(lista10[2])

#El metodo extend agrega una lista al final de otra lista, la operacion afecta a la lista invocante
nombres1 = ["Antonio","Maria","Mabel"]
nombres2 = ["Barry","John","Guttag"]
nombres3 = ["Barry","John","Guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

#Repetir
lista11 =[1,2,3,4,5]
lista12 =lista11*3
print(lista12)

#Comparacion
#Usando los operadores convencionales (<,<=,>,>=,==,!=)
print(["Rojas", 123] < ["Rosas",123])
print(["Rojas", 123] == ["rosas",123])
print(["Rojas", 123] > ["Rosas",23])

#Es posible determinar si un elemento se encuentra en una lista
lista13 =["Cien","años","de","soledad"]
if "de" in lista13
    print("Siesta en la linea")
else:
    print("No esta en la lista")

#Iterando una lista
lista15 =["hola","amigos","mios"]
for palabra in lista15: #para marcar cada palabra de la lista
    print(palabra, end=",")#parametro end envia salto de linea

#Diccionarios
diccionario ={}#diccionario bacio
#diccionario con 4 items o registros
puertos = {
    22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL"
}
print(puertos)

#El metodo update agrega items de un diccionario de entorno
puertos1 = {
    22:"SSH",
    80:"Http"
}
puertos2 = {
    53:"DNS"
    443:"Https"
}
print(puertos1)
puertos1.update(puertos2)
print(puertos1)

#Comparar
#Se mira si los diccionarios tienen los mismos items
a = {123:"Rojas", 87:"Rosas"} == {87:"Rosas",123:"Rosas",78:"Otro"}
print(a)

#Accediendo al valor de un item con la clave dada
puertos3 = {
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    3306: "MySQL"
}
protocolo = puertos3[22]
print(protocolo)
#puerto3[8080]#Error

#Eliminar item con la clave dada
calificaciones = {
    "alumno1":5,
    "alumno2":3,
    "alumno3":4,
    "alumno4":3
}
print(calificaciones)
del calificaciones["alumno3"]
print(calificaciones)

#Iterar un diccionario
#usar  el ciclo for y el metodo items para obtener los items de un diccionario
dicPuertos = {
    22:"SSH",
    23:"telnet",
    80:"Http"
}
for x,y in dicPuertos.items():
    print(x,"->",y)
    