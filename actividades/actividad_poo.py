class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=input("Ingrese la edad: ")

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

class Ciudadano(Persona):

    def __init__(self):
        super().__init__()
        self.deposito=float(input("Ingrese el dinero a depositar: "))

    def imprimir(self):
        super().imprimir()
        print("Deposito:",self.deposito)

    def impuestos(self):
        if self.deposito> 4000:
            print(f'El cuidadano {self.nombre} debe pagar impuestos')

        else:
            print(f'El ciudadano {self.nombre} no debe pagar impuestos')


#Instancias
ciudadano1=Ciudadano()
ciudadano1.imprimir()
ciudadano1.impuestos()

