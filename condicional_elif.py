'''
En una escuela de conduccion se tiene un programa que dependiendo de la edad del
usuario debe mostrar el tipo de licencia a la que tiene derecho

Condicion 1: Si es menor a 16, entonces no puedes conducir,
Condicion 2: Si es menor a 18, entonces puede obtener un permiso para conducir,
Condicion 3: Si es menor a 70, entonces puede obtener una licencia estandar,
Condicion 4: Si es mayor a 70, entonces necesita una licencia especial.
'''

edad = int(input("Digita tu edad: "))

if edad < 16:
    print ("No tienes edad para conducir.")
elif edad < 18:
    print("Puedes obtener un permiso para conducir.")
elif edad < 70:
    print("Puedes obtener una licencia estandar.")
else:
    print("Necesitas obtener una licencia especial.")

