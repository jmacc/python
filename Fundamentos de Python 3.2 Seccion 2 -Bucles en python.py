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
"""
#LA HIPOTESIS DE LOTHAR COLLATZ

c0 = -1

while c0 <= 0 :
   valor = input("Ingresa un valor entero: ")
   if valor.isdigit():
       c0 = int(valor)
       if c0 > 0:
        print("Seguimos: ",c0)
        if c0 % 2 == 0:
            print("El {} es par".format(c0))
            operacion = c0 /2
            print(operacion) #el valor de la operacion
            if operacion == 1:
                break
            else:
               c0 = operacion
            
        else:
            print("El {} es impart".format(c0))
            operacion = (c0*3)+1
            print(operacion) #el valor de la operacion
            if operacion == 1:
                break
            else:
               c0 = operacion
            
   else:
       print("Valor inválido, intenta de nuevo.")