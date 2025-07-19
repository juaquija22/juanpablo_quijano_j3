telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"#  Toma los primeros tres dígitos, luego tres más, y los últimos cuatro, y los organiza en formato (xxx) xxx-xxxx.
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")