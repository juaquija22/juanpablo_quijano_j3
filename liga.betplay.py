import os

Equipos = []
Partidos = []

def agregar_equipo():
    nombre = input("Ingrese el nombre del equipo: ").capitalize()
    equipo = {
        "nombre": nombre,
        "goles_a_favor": 0,
        "goles_en_contra": 0,
        "partidos_jugados": 0,
        "partidos_ganados": 0,
        "partidos_perdidos": 0
    }
    Equipos.append(equipo)
    print(f"Equipo agregado: {equipo}")
    os.system("pause")

def programar_fecha():
    if not Equipos:
        print("No hay Equipos Registrados.")
        os.system("pause")
        return

    print("Equipos disponibles:")
    for i, equipo in enumerate(Equipos):
        print(f"{i + 1}. {equipo['nombre']}")

    local = input("Seleccione el Equipo local (Escriba el nombre del Equipo): ").capitalize()
    visitante = input("Seleccione el Equipo visitante (Escriba el Nombre del Equipo): ").capitalize()
    nombres = [eq["nombre"] for eq in Equipos]

    if local == visitante:
        print("Un equipo no puede jugar contra sí mismo.")
        os.system("pause")
        return

    if local not in nombres or visitante not in nombres:
        print("Alguno de los equipos no está registrado.")
        os.system("pause")
        return

    fecha = input("Ingrese la fecha del partido: ")
    Partidos.append({
        "fecha": fecha,
        "local": local,
        "visitante": visitante
    })
    print(f'{Partidos}')
    os.system("pause")

def Registrar_marcador():
    if not Partidos:
        print("No hay partidos programados.")
        os.system("pause")
        return

    print("Partidos programados:")
    for i, partido in enumerate(Partidos):
        print(f"{i + 1}. {partido['local']} vs {partido['visitante']} - Fecha: {partido['fecha']}")

    try:
        registro = int(input('Seleccione el número del partido: ')) - 1
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        os.system("pause")
        return

    if registro < 0 or registro >= len(Partidos):
        print("Número fuera de rango.")
        os.system("pause")
        return

    partido = Partidos[registro]

    try:
        goles_local = int(input(f'Goles de {partido["local"]}: '))
        goles_visitante = int(input(f'Goles de {partido["visitante"]}: '))
    except ValueError:
        print("Los goles deben ser números enteros.")
        os.system("pause")
        return

    partido["goles_local"] = goles_local
    partido["goles_visitante"] = goles_visitante

    if goles_local > goles_visitante:
        print(f'{partido["local"]} ganó.')
    elif goles_local < goles_visitante:
        print(f'{partido["visitante"]} ganó.')
    else:
        print('Empate.')

    for equipo in Equipos:
        if equipo["nombre"] == partido["local"]:
            equipo["goles_a_favor"] += goles_local
            equipo["goles_en_contra"] += goles_visitante
            equipo["partidos_jugados"] += 1
            if goles_local > goles_visitante:
                equipo["partidos_ganados"] += 1
            elif goles_local < goles_visitante:
                equipo["partidos_perdidos"] += 1

        elif equipo["nombre"] == partido["visitante"]:
            equipo["goles_a_favor"] += goles_visitante
            equipo["goles_en_contra"] += goles_local
            equipo["partidos_jugados"] += 1
            if goles_visitante > goles_local:
                equipo["partidos_ganados"] += 1
            elif goles_visitante < goles_local:
                equipo["partidos_perdidos"] += 1

    os.system("pause")

def equipo_mas_goles_contra():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not Equipos:
        print("No hay equipos registrados.")
    else:
        peor_equipo = Equipos[0]
        for equipo in Equipos:
            if equipo["goles_en_contra"] > peor_equipo["goles_en_contra"]:
                peor_equipo = equipo
        print(f"Más goles en contra: {peor_equipo['nombre']} ({peor_equipo['goles_en_contra']} GC)")
    os.system("pause")

def equipo_mas_goles_favor():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not Equipos:
        print("No hay equipos registrados.")
    else:
        mejor_equipo = Equipos[0]
        for equipo in Equipos:
            if equipo["goles_a_favor"] > mejor_equipo["goles_a_favor"]:
                mejor_equipo = equipo
        print(f"Más goles a favor: {mejor_equipo['nombre']} ({mejor_equipo['goles_a_favor']} GF)")
    os.system("pause")

def registrar_planilla():
    if not Partidos:
        print("No hay partidos programados.")
        os.system("pause")
        return

    print("Partidos disponibles:")
    for i, partido in enumerate(Partidos):
        print(f"{i + 1}. {partido['local']} vs {partido['visitante']} - Fecha: {partido['fecha']}")

    try:
        seleccion = int(input("Seleccione el número del partido: ")) - 1
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        os.system("pause")
        return

    if seleccion < 0 or seleccion >= len(Partidos):
        print("Número fuera de rango.")
        os.system("pause")
        return

    partido = Partidos[seleccion]
    planilla_local = []
    planilla_visitante = []

    try:
        cantidad = int(input("¿Cuántos jugadores desea registrar por equipo? "))
    except ValueError:
        print("Debe ingresar un número.")
        os.system("pause")
        return

    print(f"Ingrese jugadores del equipo {partido['local']}:")
    for i in range(cantidad):
        jugador = input(f"Jugador {i + 1}: ")
        planilla_local.append(jugador)

    print(f"Ingrese jugadores del equipo {partido['visitante']}:")
    for i in range(cantidad):
        jugador = input(f"Jugador {i + 1}: ")
        planilla_visitante.append(jugador)

    partido["planilla_local"] = planilla_local
    partido["planilla_visitante"] = planilla_visitante

    print("Planillas registradas correctamente.")
    os.system("pause")

def main_menu() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menú:")
    print("1. Registrar Equipo")
    print("2. Programar Fecha")
    print("3. Registrar Marcador")
    print("4. Equipo con más goles en contra")
    print("5. Equipo con más goles a favor")
    print("6. Registrar Planilla")
    print("7. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número.")
        os.system("pause")
        return main_menu()

    if opcion < 1 or opcion > 7:
        print("Opción inválida.")
        os.system("pause")
        return main_menu()

    return opcion

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de equipos")
        opcion = main_menu()

        match opcion:
            case 1:
                agregar_equipo()
            case 2:
                programar_fecha()
            case 3:
                Registrar_marcador()
            case 4:
                equipo_mas_goles_contra()
            case 5:
                equipo_mas_goles_favor()
            case 6:
                registrar_planilla()
            case 7:
                print("has salido")
                os.system("pause")
                break




