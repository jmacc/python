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
'''
def message(number):
    print("Ingresa un número:", number)
    
number = 1234
message(1)
print(number)