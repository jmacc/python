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
        
##############################################

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
##############################################

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))

#Tu tarea es escribir una función que verifique si un número es primo o no.
#La función:
#se llama is_prime;
#toma un argumento (el valor a verificar)
#devuelve True si el argumento es un número primo, y False de lo contrario.
##

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

##############################################

#Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.
#Las funciones:
#se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
#toman un argumento (el valor correspondiente a sus nombres)
# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
##############################################

def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # salida: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # salida: None
##############################################

def wishes():
    return "¡Felíz Cumpleaños!"
 
w = wishes()
 
print(w) # salida:¡Felíz Cumpleaños!
##############################################
# Ejemplo 1
def wishes():
    print("Mis deseos")
    return "Felíz Cumpleaños"
 
wishes() # salida: Mis deseos
 ##############################################
 
# Ejemplo 2
def wishes():
    print("Mis deseos")
    return "Felíz Cumpleaños"
 
print(wishes())
 
# salida: Mis deseos
# Felíz Cumpleaños
##############################################
def hi_everybody(my_list):
    for name in my_list:
        print("Hola,", name)
 
hi_everybody(["Adán", "Juan", "Lucía"])
##############################################
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
############################################## 
print(create_list(5))

def hi():
    return
    print("¡Hola!")
 
hi() #none
##############################################

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False
 
print(is_int(5)) #true
print(is_int(5.0)) #false
print(is_int("5")) #none

##############################################
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
 
print(even_num_lst(11)) #[0, 2, 4, 6, 8, 10]
##############################################

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
 
foo = [1, 2, 3, 4, 5]
print(list_updater(foo)) #[1, 4, 9, 16, 25]
##############################################

def my_function():
    var = 2
    print("¿Conozco a la variable?", var)
 
var = 1
my_function()
print(var)
##############################################
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)

var = 1
my_function()
print(var)
##############################################
def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


var = 1
my_function(var)
print(var)
##############################################

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

##############################################

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
##############################################

#Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.
#(Ejemplo 1) al menos que la función defina una variable con el mismo nombre. (Ejemplo 2, y Ejemplo 3),
#ejemplo 1
var = 2
def mult_by_var(x):
    return x * var
print(mult_by_var(7)) # salida: 14

##############################################
#ejemplo 2
def mult(x):
    var = 5
    return x * var
 
print(mult(7)) # salida: 35
##############################################

#ejemplo 3
def mult(x):
    var = 7
    return x * var
 
 
var = 3
print(mult(7)) # salida: 49

##############################################
def adding(x):
    var = 7
    return x + var
 
 
print(adding(4)) # salida: 11
print(var) # NameError
##############################################

var = 2
print(var) # salida: 2
 
def return_var():
    global var
    var = 5
    return var
 
print(return_var()) # salida: 5
print(var) # salida: 5
##############################################

def message():
    alt = 1
    print("¡Hola, mundo!")
print(message())
a = 1
##############################################

def fun():
    global a
    a = 2
    print(a)
fun()
a = 3
print(a)
##############################################
'''