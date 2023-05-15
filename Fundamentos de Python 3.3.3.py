#Fundamentos de Python 3.3 Seccion 3 -Operaciones lógicas y de bits en Python
""" 
#counter > 0 and value == 100

# Ejemplo 1:
print(var > 0)
print(not (var <= 0))
 
 
# Ejemplo 2:
print(var != 0)
print(not (var == 0))
##############################################
 
''' 
Los operadores lógicos toman sus argumentos como un todo, independientemente de cuantos bits contengan. 
Los operadores solo conocen el valor: cero (cuando todos los bits se restablecen) 
significa False; no cero (cuando se establece al menos un bit) significa True.
'''
i = 0
j = not not i
print(j)
##############################################

# Ejemplo 1:
var = 5
print(var > 0)
print(not (var <= 0))


# Ejemplo 2:
print(var != 0)
print(not (var == 0))
##############################################

print(bin(27))
# 0b11011
##############################################

a = 0b1101
b = 0b1011
print(bin(a & b))
#0b1001
##############################################

a = 40
print(bin(a))
print(bin(~a))
#0b101000
#-0b101001
##############################################

x = 0b0110 ^ 0b1010
print(bin(x))
# 0 xor 1 = 1
# 1 xor 0 = 1
# 1 xor 1 = 0
# 0 xor 0 = 0
# 0b1100
##############################################

a=0b1000
print(bin(a>>2))
# 0b10
##############################################

a=0b0001
print(bin(a<<3))
# 0b1000
##############################################

a=0b0001
print(bin(a<<10))
# 0b10000000000
##############################################

#print(4<<1)

'''
1. Python es compatible con los siguientes operadores lógicos:

and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.
2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:

x = 15, el cual es 0000 1111 en binario,
y = 16, el cual es 0001 0000 en binario.
Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:

& hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
| hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,
^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
>> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
<< hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = , el cual es 1000 0000 en binario.
* -16 (decimal del complemento a 2 con signo) -- lee más acerca de la operación Complemento a dos.
'''
#quiz
x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(x == y) and (x == y)
print(z)
print(not(z))

##############################################
"""
x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)