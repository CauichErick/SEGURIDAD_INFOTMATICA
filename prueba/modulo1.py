def tabla():
    inicio_rango = int(input("ingresa el inicio_rango: "))
    final_rango = int(input("ingresa el final_rango: "))
    inicio_tabla = int(input("ingresa el inicio_tabla: "))
    final_tabla = int(input("ingresa el final_tabla: "))

    for i in range(inicio_rango, final_rango + 1):
        for mul in range(inicio_tabla, final_tabla + 1):
            print(f"{i} * {mul} = {i * mul}")
        print()
        