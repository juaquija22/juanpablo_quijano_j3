frase = input("Escribe una frase: ") #input solicita al usuario que ingrese un dato
total_caracteres = len(frase) # len cuenta en numero de caracteres en la cadena
espacios = frase.count(" ") # count cuenta el numero de " " en la cadena

print(f"La frase tiene {total_caracteres} caracteres en total.") # imprime el total de caracteres 
print(f"La frase tiene {espacios} espacios.") # imprime el total de espacios