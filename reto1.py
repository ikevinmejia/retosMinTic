print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

user = int(input("Ingrese el número de usuario: "))

if user == 1234:
    password = int(input("Ingrese la contraseña: "))
    if password == 4321:
        print("¿Eres un robot?")
        print("¿Cuál es el resultado de los siguientes capchat")
        cap1 = 321
        cap2 = 234
        cap3 = cap1 + cap2
        cap4 = cap1 * 2
        result = int(input("321 + 234 = "))
        result2 = int(input("321 * 2 = "))
        if result == cap3 and result2 == cap4:
            print("Sesión iniciada")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")