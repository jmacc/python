#Fundamentos de python Seccion 6 - Interaccion con el usuario
#########################################
"""
x = int(input("Ingresa un número: ")) # El usuario ingresa un 2
print(x * "5") #Imprime 2 veces el mismo numero
print(type(x)) #imprime el tipo de valor
#########################################
b = input("Ingresa un número: ") # El usuario ingresa un 2
print(type(b)) #imprime el tipo de valor
#########################################
print(x,'^12=', x**12)#valor a una potencia
print(1//2*3)
print()
#########################################
x = 1
y = 2
z = x #1
x = y #2
y = z #1
print(x, y)
##########################################

x = int(input())
y = int(input())
 
x = x // y
y = y // x  #marca error
 
print(y)
##########################################

x = int(input())
y = int(input())
 
x = x / y
y = y / x
 
print(y) #imprimwe 8
##########################################


x = int(input())
y = int(input())
 
x = x % y
x = x % y
y = y % x
 
print(y) imprime 1
##########################################

z = y = x = 1
print(x, y, z, sep='*') #es 1*1*1*
##########################################

y = 2 + 3 * 5.
print(Y)
##########################################

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x) #es 17.5
##########################################

x = int(input())
y = int(input())
 
print(x + y) # es 6
##########################################
"""
x = input()
y = int(input())
 
print(x * y) #imprime 333333