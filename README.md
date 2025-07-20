# Readme

## *Ejercicio 1*

### **Línea 1**

**Función:**  input()
 **¿Qué hace?:** 

Muestra un mensaje en pantalla y espera que el usuario escriba una frase
 **¿Qué guarda?:**

 Guarda el texto ingresado por el usuario en la variable  = frase

------

### **Línea 2**

**Función:**  len()

**¿Qué hace?: **

 Cuenta la cantidad total de caracteres en la frase 
 **¿Qué guarda?:**

Guarda ese número en la variable = total_caracteres.

------

### **Línea 3**

**Función:**  count(" ")
 **¿Qué hace?**

 Cuenta cuántas veces aparece el carácter espacio " " en la frase.
 **¿Qué guarda?:**

 Guarda ese número en la variable espacios.

------

### **Línea 4**

**Función:** print()  y  f""
 **¿Qué hace?:** 

Muestra en pantalla el mensaje junto con el valor de  total_caracteres

------

### **Línea 5**

**Función:** print()  y  f""
 **¿Qué hace?:**

 Muestra en pantalla el mensaje junto con el valor de espacios



## *Ejercisio 2*

### **Línea 1**

**Función:** input()
 **¿Qué hace?:**
 Muestra un mensaje en pantalla y espera que el usuario escriba su nombre completo.
 **¿Qué guarda?:**
 Guarda el texto ingresado por el usuario en la variable nombre.

------

### **Línea 2**

**Función:** .replace(" ", "").isalpha()
 **¿Qué hace?:**
 Elimina los espacios del texto y verifica si solo quedan letras, sin números ni símbolos.
 

------

### **Línea 3**

**Función:** .istitle()
 **¿Qué hace?:**
 Verifica si cada palabra del nombre comienza con mayúscula y el resto de letras están en minúscula.
 

------

### **Línea 4**

**Función:** print()
 **¿Qué hace?:**
 Muestra el mensaje "El nombre es válido." si cumple todas las condiciones.

------

### **Línea 5**

**Función:** print()
 **¿Qué hace?:**
 Muestra el mensaje "El nombre debe comenzar con mayúscula." si contiene solo letras pero no está bien escrito.

------

### **Línea 6**

**Función:** print()
 **¿Qué hace?:**
 Muestra el mensaje "El nombre solo debe contener letras." si el texto contiene números u otros símbolos.



## Ejercicio 3

### **Línea 1**

**Función:**  input()
 **¿Qué hace?:**
 Muestra el mensaje "Escribe una palabra: " y espera que el usuario escriba una palabra.
 **¿Qué guarda?:**
 Guarda el texto ingresado por el usuario en la variable palabra.

------

### **Línea 2**

**Función:** [::-1] 
 **¿Qué hace?:**
 Invierte el orden de los caracteres de la palabra.
 **¿Qué guarda?:**
 Guarda la palabra invertida en la variable invertida.

------

### **Línea 3**

**Función:** print() y f""
 **¿Qué hace?:**
 Muestra en pantalla la palabra invertida dentro de un mensaje.

# Ejercicio 4

### **Línea 1**

**Función:** input()
 **¿Qué hace?:**
 Muestra el mensaje Escribe una frase: y espera que el usuario escriba una frase.
 **¿Qué guarda?:**
 Guarda el texto ingresado por el usuario en la variable frase.

------

### **Línea 2**

**Función:** .replace(a, *).replace(e, *).replace(i, *).replace(o, *).replace(u, *)
 **¿Qué hace?:**
 Reemplaza todas las vocales minúsculas a, e, i, o, u por el símbolo * una por una en cadena.
 **¿Qué guarda?:**
 Guarda el resultado (con vocales minúsculas reemplazadas) en la variable frase_cifrada.

------

### **Línea 3**

**Función:** .replace(A, *).replace(E, *).replace(I, *).replace(O, *).replace(U, *)
 **¿Qué hace?:**
 Reemplaza todas las vocales mayúsculas A, E, I, O, U por el símbolo * una por una.
 **¿Qué guarda?:**
 Actualiza la variable frase_cifrada con las vocales mayúsculas también cifradas.

------

### **Línea 4**

**Función:** print() y f""
 **¿Qué hace?:**
 Muestra en pantalla el mensaje La frase cifrada es: seguido de la frase con todas las vocales reemplazadas por *.

# Ejercicio 5

### **Línea 1**

**Función:** input()
 **¿Qué hace?:**
 Muestra el mensaje Escribe una frase: y espera que el usuario escriba una frase.
 **¿Qué guarda?:**
 Guarda el texto ingresado por el usuario en la variable frase.

------

### **Línea 2**

**Función:** count(a) y count(A)
 **¿Qué hace?:**
 Cuenta cuántas veces aparece la letra a (mayúscula y minúscula) en la frase.
 **¿Qué guarda?:**
 Guarda la cantidad total de letras a en la variable a.

------

### **Línea 3**

**Función:** count(e) y count(E)
 **¿Qué hace?:**
 Cuenta cuántas veces aparece la letra e (mayúscula y minúscula) en la frase.
 **¿Qué guarda?:**
 Guarda la cantidad total de letras e en la variable e.

------

### **Línea 4**

**Función:** count(i) y count(I)
 **¿Qué hace?:**
 Cuenta cuántas veces aparece la letra i (mayúscula y minúscula) en la frase.
 **¿Qué guarda?:**
 Guarda la cantidad total de letras i en la variable i.

------

### **Línea 5**

**Función:** count(o) y count(O)
 **¿Qué hace?:**
 Cuenta cuántas veces aparece la letra o (mayúscula y minúscula) en la frase.
 **¿Qué guarda?:**
 Guarda la cantidad total de letras o en la variable o.

------

### **Línea 6**

**Función:** count(u) y count(U)
 **¿Qué hace?:**
 Cuenta cuántas veces aparece la letra u (mayúscula y minúscula) en la frase.
 **¿Qué guarda?:**
 Guarda la cantidad total de letras u en la variable u.

------

### **Línea 7**

**Función:** suma
 **¿Qué hace?:**
 Suma todas las vocales a, e, i, o, u para obtener el total.
 **¿Qué guarda?:**
 Guarda el total de vocales en la variable total_vocales.

------

### **Línea 8**

**Función:** print() y f""
 **¿Qué hace?:**
 Muestra en pantalla el mensaje La frase tiene X vocales, donde X es el valor de total_vocales.



# Ejercicio 6

### **Línea 1**

**Función:** input()
 **¿Qué hace?:**
 Muestra el mensaje Escribe un número de teléfono de 10 dígitos: y espera que el usuario escriba un número.
 **¿Qué guarda?:**
 Guarda el número ingresado por el usuario en la variable telefono.

------

### **Línea 2**

**Función:** len() y isdigit()
 **¿Qué hace?:**
 Verifica que el número tenga exactamente 10 caracteres y que todos sean dígitos.
 **¿Qué guarda?:**
 No guarda nada, es una condición lógica para ejecutar o no el bloque de código siguiente.

------

### **Línea 3**

**Función:** slicing [:3], [3:6], [6:] y f""
 **¿Qué hace?:**
 Toma los primeros tres dígitos, luego tres más, y los últimos cuatro, y los organiza en formato (xxx) xxx-xxxx.
 **¿Qué guarda?:**
 Guarda el número formateado en la variable telefono_formateado.

------

### **Línea 4**

**Función:** print() y f""
 **¿Qué hace?:**
 Muestra en pantalla el mensaje El número formateado es: seguido del valor de telefono_formateado.

------

### **Línea 5**

**Función:** else
 **¿Qué hace?:**
 Ejecuta un mensaje alternativo si la condición del if no se cumple.
 **¿Qué guarda?:**
 No guarda nada.

------

### **Línea 6**

**Función:** print()
 **¿Qué hace?:**
 Muestra el mensaje El número debe tener exactamente 10 dígitos.



# Ejercicio 7

### **Línea 1**

**Función:** input() y lower()
 **¿Qué hace?:**
 Muestra el mensaje Escribe una palabra: y convierte el texto ingresado a minúsculas.
 **¿Qué guarda?:**
 Guarda la palabra en minúsculas en la variable palabra.

------

### **Línea 2**

**Función:** [::-1] (slicing invertido)
 **¿Qué hace?:**
 Invierte el orden de los caracteres de la palabra.
 **¿Qué guarda?:**
 Guarda la palabra invertida en la variable invertida.

------

### **Línea 3**

**Función:** == (comparación)
 **¿Qué hace?:**
 Compara si la palabra original es igual a su versión invertida.
 **¿Qué guarda?:**
 No guarda nada, es una condición para ejecutar un bloque de código.

------

### **Línea 4**

**Función:** print()
 **¿Qué hace?:**
 Muestra el mensaje La palabra es un palíndromo.

------

### **Línea 5**

**Función:** else
 **¿Qué hace?:**
 Ejecuta una acción alternativa si la palabra no es igual a su versión invertida.
 **¿Qué guarda?:**
 No guarda nada.

------

### **Línea 6**

**Función:** print()
 **¿Qué hace?:**
 Muestra el mensaje La palabra no es un palíndromo.

