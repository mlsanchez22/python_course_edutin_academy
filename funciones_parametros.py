'''
def es_par(numero):
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')

es_par(5)


def saludar(nombre):
    print("Hola " + nombre + " eres el mejor programador")
saludar("Jose")


def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a - b

resultado = resta(1,2)
print(resultado)
'''

def multiplicacion(numero = None):
    if numero == None:
        print("Por favor, introduce un número")
    else:
        print(f'TABLA DE MULTIPLICAR DEL {numero}')
        for i in range(1,11):
            print(f'{i} x {numero} = {i * numero}')

multiplicacion(2)
