'''
Escribir un programa que almacena las asignaturas de un curso

asignaturas = ["Matemáticas","Física","Español","Inglés"]

print(asignaturas[2])
print(type(asignaturas))

#Loteria
numeros=[]

for i in range(6):
    numeros.append(int(input("Introduce un número: ")))

numeros.sort()
print(f'Los números ganadores son: {numeros}')
'''

lista = [1,4,5,6,7,8,6,"Hola"]

for i in lista:
    print(i)

#lista.remove(6)
#lista.pop(7)
#del lista[0]
#lista.clear()

#print("Esta es la lista después de colocar el método clear:" + str(lista))
#for i in lista:
#    print(i)

#print(lista.count(1))
#print(lista.index("Hola"))
lista.reverse()
print(lista)