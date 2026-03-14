equipos = {}

while True:
    print("MENU: Torneo de Futbol")
    print("1. Agregar equipo")
    print("2. Registrar resultado")
    print("3. Mostrar tabla de posiciones")
    print("4. Eliminar equipo")
    print("5. Salir")

    opcion = input("Opcion: ")
    if opcion == "1":
        nombre = input("Escribi el nombre del equipo: ")
        if nombre in equipos:
            print("Error: este equipo ya existe en el torneo.")
        else:
            equipos[nombre] = 0
            print("Equipo agregado con exito.")

    elif opcion == "2":
        local = input("Escribi el equipo local: ")
        visitante = input("Escribi el equipo visitante: ")

        if local not in equipos or visitante not in equipos:
            print("Error: Uno o ambos equipos no estan registrados.")
            continue

        resultado = input("Marcador: ")
        partes = resultado.split("-")

        if len(partes) != 2:
            print("Error: Formato invalido. Formato correcto X - Y.")
            continue

        goles_local_str = partes[0].strip()
        goles_visitante_str = partes[1].strip()

        # verificar que se ingresne nros
        if not goles_local_str.isdigit() or not goles_visitante_str.isdigit():
            print("Error: Los goles tienen que ser numeros positivos.")
            continue

        goles_local = int(goles_local_str)
        goles_visitante = int(goles_visitante_str)

        if goles_local > goles_visitante:
            equipos[local] += 3
        elif goles_visitante > goles_local:
            equipos[visitante] += 3
        else:
            equipos[local] += 1
            equipos[visitante] += 1

        print("Resultado registrado correctamente.")

    elif opcion == "3":
        if len(equipos) == 0:
            print("Todavia no hay equipos registrados.")
        else:
            tabla_ordenada = []
            for equipo in equipos:
                puntos = equipos[equipo]
                tabla_ordenada.append([puntos, equipo])

            # reverse=True ==> mayor a menor
            tabla_ordenada.sort(reverse=True)

            print("TABLA DE POSICIONES")
            for fila in tabla_ordenada:
                puntos = fila[0]
                equipo = fila[1]
                print(f"{equipo}: {puntos} puntos")

    elif opcion == "4":
        nombre = input("Escribi el nombre del equipo a eliminar: ")
        if nombre in equipos:
            del equipos[nombre]
            print("Equipo eliminado del torneo.")
        else:
            print("Error: El equipo no existe.")

    elif opcion == "5":
        print("Fin del programa")
        break

    else:
        print("Opcion invalida. Elegi un nro del 1 al 5.")
