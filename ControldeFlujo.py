#ControldeFlujo

#Sentenciaif
numero =int(input("Escribe un numero del 1 al 10 "))
if numero > 5:
    print("El numero "+str(numero)+" Es mayor a 5")
print("Escribiste el numero "+str(numero))

#sentencia if else

cadena_ejemplo="en un lugar de la mancha"
palabra="lugar"
if palabra in cadena_ejemplo:
    print ("Encontrado la palabra! ->"+palabra)
else:
    print ("No encontrado la palabra -> !!! "+palabra)
    
#-----------------------------------------------------
if cadena_ejemplo.startswith("l"):
    print("Stars with letter l")
else:
    print("Not stars with letter l")

#-----------------------------------------------------
#sentencia if else if
numero1=int(input("Ingresa el primer numero"))
numero2=int(input("Ingresa segundo numero"))
if numero1 > numero2:
    print("El primer numero es mayor que el segundo")
elif numero1 == numero2:
    print("Los numeros son iguales")
else:
    print("El  primer numero "+str(numero1)+" es menor que el segundo "+str(numero2))