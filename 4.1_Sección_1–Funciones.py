#4.1 Sección 1 - Funciones
'''

def message():
    print("Ingresar valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

##############################################

def hello(name): # definiendo una función
    print("Hello,", name) # cuerpo de la función
 
 
name = input("Ingresa tu nombre: ")
 
hello(name) # invocación de la función

##############################################

def message(number):
    print("Ingresa un número:", number)
    
number = 1234
message(1)
print(number)
##############################################

def message(what, number):
    print("Ingresa", what, "número", number)
 
message("teléfono", 11)
message("precio", 5)
message("número", "number")
##############################################

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(last_name="Skywalker", first_name="Luke")
introduction(last_name="Quick", first_name="Jesse")
introduction(last_name="Kent", first_name="Clark")

##############################################

def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)
introduction("Enrique")

#Ejemplo 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # salida: 3
subtra(2, 5) # salida: -3
 
 
#Ejemplo 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # salida: 3
subtra(b=2, a=5) # salida: 3
 
#Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # salida: 3
subtra(5, 2) # salida: 3

#Ejemplo
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # salida: 3
subtra(a=5, 2) # Syntax Error

#Es importante recordar que primero 
#se especifican los argumentos posicionales y después los de palabras clave.

##############################################

def add_numbers(a, b=2, c): #esta seccion marca error
    print(a + b + c)
 
add_numbers(a=1, c=3)
##############################################
#Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:
#cuando se le asigna a una variable (o se devuelve como el resultado de una función)
#cuando se compara con una variable para diagnosticar su estado interno.

value = None
if value is None:
    print("Lo siento, no contienes ningún valor")
    

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(15))
print(strange_function(10))

##############################################

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
print(list_sum([5, 4, 3]))

##############################################

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

##############################################
'''
#Tu tarea es escribir y probar una función que toma un argumento (un año) 
#y devuelve True si el año es un año bisiesto, o False si no lo es.
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, True]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("fallido")