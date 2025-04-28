'''
Primer ejemplo:
Crear un programa que reciba el número de años que tiene nuestra computadora
Imprimir nuestra consola si es nuevo o es viejo.
Condiciones: Si es menor o igual a 2 años, entonces es nuevo.
Pero, si es mayor a 2 años, entonces es viejo.


anios = int(input("¿Cuántos años tiene tu computador? "))

if anios >= 0 and anios <= 2:
    print("Tu computador es nuevo")

else:
    print("Tu computador es viejo")

'''

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Es usted mayor de edad")
else:
    print("Es usted menor de edad")

print ("Hasta la proxima!")