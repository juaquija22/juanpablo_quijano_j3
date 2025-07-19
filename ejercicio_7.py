palabra = input("Escribe una palabra: ").lower() # Muestra el mensaje Escribe una palabra: y convierte el texto ingresado a minúsculas.
invertida = palabra[::-1] # Escribe la palabra al reves

if palabra == invertida:
    print("La palabra es un palíndromo.") # 
else:
    print("La palabra no es un palíndromo.")