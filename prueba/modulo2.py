def informacion_p():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    correo = input("Ingresa tu correo: ")
    numero = input("Ingresa tu número de teléfono: ")

    informacion = {
        'Nombre': nombre,
        'Edad': edad,
        'Correo': correo,
        'Número de teléfono': numero
    }

    print("Información guardada exitosamente. Aquí está la información que proporcionaste:")
    print(f" su nombre es:{nombre} y su numero {numero}")
