frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A") # cuenta las vocales mayusculas y minusculas de la a y A
e = frase.count("e") + frase.count("E") # cuenta las vocales mayusculas y minusculas de la e y E
i = frase.count("i") + frase.count("I") # cuenta las vocales mayusculas y minusculas de la i y I
o = frase.count("o") + frase.count("O") # cuenta las vocales mayusculas y minusculas de la o y O
u = frase.count("u") + frase.count("U") # cuenta las vocales mayusculas y minusculas de la u y U

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")