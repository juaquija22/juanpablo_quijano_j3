nombre = input("Escribe tu nombre completo: ") #input solicita al usuario que ingrese un dato

if nombre.replace(" ", "").isalpha(): # Elimina los espacios del texto y verifica si solo quedan letras, sin números ni símbolos.
    if nombre.istitle(): #
        print("El nombre es válido.") # Verifica si cada palabra del nombre comienza con mayúscula y el resto de letras están en minúscula.
    else:
        print("El nombre debe comenzar con mayúscula.") #
else:
    print("El nombre solo debe contener letras.") #