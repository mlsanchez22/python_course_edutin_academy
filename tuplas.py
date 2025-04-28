'''
Crear una tupla con números y
luego pedir un número por teclado
e indicar cuantas veces se repite
'''

numeros = (5,6,7,8,5,5,98,12,14,12)

numero = int(input("Dame un número: "))

#print("El número se repite: " + str(numeros.count(numero)) + " veces.")

print("El número " + str(numero) + " se encuentra en el índice: " + str(numeros.index(numero)))