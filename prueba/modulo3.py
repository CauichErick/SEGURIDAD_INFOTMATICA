def promedio():
    calificacion1 = float(input("Ingresa la primera calificación: "))
    calificacion2 = float(input("Ingresa la segunda calificación: "))
    calificacion3 = float(input("Ingresa la tercera calificación: "))
    calificacion4 = float(input("Ingresa la cuarta calificación: "))
    calificacion5 = float(input("Ingresa la quinta calificación: "))

    promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

    return(promedio)
print("El promedio de las 5 calificaciones es:", promedio)
