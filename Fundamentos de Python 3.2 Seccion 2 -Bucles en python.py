#Fundamentos de Python 3.2 Seccion 2 -Bucles en python
""" 
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)
##############################################

#Ejemplo 2
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
#while number != 0: #es equivalene a la siguiente linea
while number:

    # Verificar si el número es impar.
    #if number % 2 == 1: #Es equivalente a la siguiente linea
    if number % 2:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)
##############################################

#Ejemplo 3
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
##############################################

datos = []
while True:
    entrada = input(">>> ")
    if entrada.strip(): #si contiene algo es True, de lo contrario False
        datos.append(entrada) #agregamos en caso contenga algo
    else:
        break #detenemos el ciclo for
#unimos todo mediante un salto de línea
print("\n".join(datos))
##############################################

#Ejercicio del numero secreto

secret_number = 777
#Se usa una impresion multilinea con 3 comillas dobles
print(
""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
"")
number = int(input("Ingresa el valor :"))
while secret_number:
    if number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Ingresa el valor :"))
##############################################

#Ejemplo d for
for i in range(10):
    print("El valor de i es", i)
##############################################

#El tercer argumento es un incremento - es un valor agregado para 
#controlar la variable en cada giro del bucle (como puedes sospechar, el valor predeterminado del incremento es 1).
for i in range(2, 8, 3):
    print("El valor de i es", i)
##############################################

for i in range(1, 1):
    print("El valor de i es", i)

##############################################

#Ejercicio del Missisipi
import time
number = 0
for i in range(5):
    time.sleep(i)
    print("Contando "+str(number)+" missisipi")
    number += 1
##############################################

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
##############################################

# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

##############################################

#Elimiacion por indice con DEL
m = ["a","A",34,0.56,"b"]
del(m[2]) #3eliminacion 34
print(m)

##############################################

#Eliminacio0n por indice con POP
m = ["a","A",34,0.56,"b"]
m.pop(2) #3eliminacion del 2 elemento que es 34
print(m)
m.pop() #Elimina del ultimo elemento que es b
print(m)

##############################################

#Eliminacio0n por su valor
m = ["a","A",34,0.56,"b"]
m.remove("A") #3eliminacion
print(m)
##############################################

#Devorador de vocales
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
#print(user_word) #str
#print(type(user_word)) #str
#list_word = list(word)
#print(list_word)
#print(type(list_word)) #list
#list_word.remove("A")
#print(list_word) #IMPRIME SIN EL VALOR ENCONETRADO
user_word = input("Ingresa una palabra: ")
word = user_word.upper()
list_word = list(word)
print("El valor de list ",list_word)
vocales = ["A","E","I","O","U"]
for letra in word:  # Completa el cuerpo del bucle for
    print("El valor de letras",letra)
    if letra in vocales:
        list_word.remove(letra)
print(list_word)
##############################################

#3.2.12 El bucle while y el bloque else

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

##############################################

#3.2.13 El bucle for y el bloque else

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
##############################################

#La piramide
blocks = int(input("Ingresa el número de bloques: "))
for i in range(blocks):
    espacios = blocks - i - 1
    asteriscos = 1 + i *2
    print(" " * espacios + "*" * asteriscos)    
#print("La altura de la pirámide:", height)

##############################################

#LA HIPOTESIS DE LOTHAR COLLATZ
'''
Para todo numero entero positivo:
    - si es par se divide entre 2
    - Si es impart se multiplica por 3 y se suma 1
    - Llevando a cabos operaciones sobre el numero resultante, 
    como resultado final siempre se alzanza el numero 1
'''
sec = []
c0 = -1
while c0 <= 0: #mientras sea positivo
    valor = input("Ingresa un valor entero: ")
    if valor.isdigit():  # si es numero
        c0 = int(valor)  # si es un numero entero
        if c0 > 0:  # si es mayor a cero
            print("Los valores de : ", c0)
            sec.append(c0) #agregamos el valor ingresado a la lista
            while c0 > 1: #ciclo de la operacion
                if c0 % 2 == 0:
                    c0 = c0 // 2
                    sec.append(c0)#agregafmos cada valor a la lista
                else:
                    c0 = (c0*3)+1
                    sec.append(c0)
        print(sec)
        print("La cantidad de pasos fueron: ",len(sec)) #obtenemos la cantidad de elementos de la lista
        
##############################################

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
##############################################

n = 0
 
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
 
print()
 
for i in range(0, 3):
    print(i)
else:
    print(i, "else")
##############################################

for i in range(6, 1,-1):
    print(i, end=" ")  # si pongo -2 output: 6, 4, 2
##############################################

#Quiz un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
##############################################

#Quiz     bucle while que cuente de 0 a 10, e imprima números impares en la pantalla
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
##############################################

#Quiz  programa con un bucle for y una sentencia break. 
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
##############################################

#Quiz un bucle for y una sentenciacontinue. El programa debe iterar sobre una cadena de dígitos,
# reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
##############################################

n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
##############################################

n = range(4)
 
for num in n:
    print(num - 1)
else:
    print(num)
##############################################
"""