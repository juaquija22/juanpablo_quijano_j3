frase = input("Escribe una frase: ")

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*") #Remplaza las vocales en minuscula por un *
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*") # Remplaza las vocales en mayuscula por un *

print(f"La frase cifrada es: {frase_cifrada}")