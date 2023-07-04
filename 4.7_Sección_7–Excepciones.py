#4.7 Sección 7 – Excepciones
##############################################
'''

try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

    
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La div210000000000000000000000000isión entre cero no está permitida en nuestro Universo.') 

##############################################
  
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer')
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except TypeError:
    print('Ha sucedido algo extraño, ¡lo siento!')
##############################################

# Se intenta abrir un fichero y se captura una posible excepción
try:
    with open('fichero.txt') as file:
        read_data = file.read()
except:
    # Se entra aquí si no pudo ser abierto
    print('No se pudo abrir')
##############################################

try:
    # Forzamos excepción
    x = 2/0
except:
    # Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
    # También entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")

#Entra en except, ha ocurrido una excepción
#Entra en finally, se ejecuta el bloque finally

# Se intenta abrir un fichero y se captura una posible excepción
##############################################

try:
    with open('fichero.txt') as file:
        read_data = file.read()
# Capturamos una excepción concreta
except OSError:
    print('OSError. No se pudo abrir')

##############################################

try:
    print("Hola"))
except SyntaxError:
    print("Hay un error de sintaxis")
    
##############################################

while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor incorrecto o se ha roto la regla de división entre cero.")
    except:
        print("Lo siento, algo salió mal...")
        ##############################################

try:
    value = int(input("Ingresa un número entero: "))
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except:
    print("¡Buuuu!")
##############################################    
 
value = input("Ingresa un número entero: ")
print(10/value)
##############################################    

def function(x=0):
    return x

d = function(10)
print(d)
##############################################    

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(3))
##############################################    

def fun(x):
    x += 1
    return x
x = 2
x = fun(x + 1)
print(x)
##############################################    

dictionary = {}
my_list = ['a', 'b', 'c', 'd']
 
for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )
 
for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k['0'])
##############################################    
   
def func(a, b):
    return a ** a
print(func(2))
##############################################    

def func_1(a):
    return a ** a

def func_2(a):
    return func_1(a) * func_1(a)
 
print(func_2(2))
##############################################    

def fun(a=b=0):
    print()
##############################################    

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(fun(fun(2)) + 1)
##############################################    

def fun(x):
    global y
    y = x * x
    return y
 
fun(2)
print(y)
##############################################    

def any():
    print(var + 1, end='')
 
var = 1
any()
print(var)
##############################################    

my_tuple = [1,2,3]
my_tuple[1] = my_tuple[1] + my_tuple[0]
print(my_tuple[1])
##############################################    

my_list = ['Mary', 'had', 'a', 'little', 'lamb']
 
def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'
 
print(my_list(my_list))
##############################################    

def fun(x, y, z):
    return x + 2 * y + 3 * z
 
print(fun(0, z=1, y=3))
##############################################    

def fun(inp=2, out=3):
    return inp * out
 
print(fun(out=2))
##############################################    

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
 
print(v)
##############################################    

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
##############################################    
'''
try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")
 