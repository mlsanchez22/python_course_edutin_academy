'''
edad = int(input("¿Cuántos años tienes? "))
graduacion = input("¿Ya te has graduado? (si) o (no) " )

if edad > 18:
    print("Felicidades! Ya tienes la mayoria de edad")
    if graduacion == "si":
        print("Felicidades por tu graduaciòn!")
'''

password = input("Ingresa la contraseña: ")

if (len(password) >= 8):
    print("Muy bien, contraseña suficientemente larga")

    if (password == 'Prueba12345'):
        print("Además, es la contraseña correcta")
    else:
        print("Pero es incorrecta")
else:
    print("Tu contraseña es incorrecta e insegura")



