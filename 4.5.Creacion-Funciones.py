#4.5.1 Ejemplos de funciones
'''
##############################################
#Calculo de IMC
def bmi(weight,height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

##############################################

#CALCULO DEL TRINGULO
#v1
def is_a_triangle(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

#v2
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

#v3
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')
############################################## 
  
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 if a > b and a > c:
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
############################################## 

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # probando
    print(n, factorial_function(n))
############################################## 

#fibonacci
  
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # probando
    print(n, "->", fib(n))
############################################## 
 
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

############################################## 

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))

############################################## 

# Implementación recursiva de la función factorial.
 
def factorial(n):
    if n == 1: # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24
############################################## 

def factorial(n):
    return n * factorial(n - 1)
 
#La función no tiene una condición de terminación, por lo tanto Python arrojara 
# una excepción (RecursionError: maximum recursion depth exceeded)
print(factorial(4))

############################################## 
''' 
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))