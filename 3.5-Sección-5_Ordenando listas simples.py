#3.5 Sección 5 – Ordenando listas simples: el ordenamiento de burbuja
##############################################
''' 
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
dato1= range(len(my_list))
print("Lista desordenada ",my_list)
print("Rango ",dato1)

##############################################

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

##############################################
# my_list[start:end]

# Copiando la lista completa.
list_1 = [1,4,7,3,5,6,3,2]
list_2 = list_1[:]
list_1[0] = 2
print(list_1)

# Copiando parte de la lista.
my_list = [10, 81, 64, 54, 82]
new_list = my_list[1:3]
print(new_list)

##############################################
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) #[8, 6, 4]


##############################################
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1] #es lo mismo my_list[:end]  0  my_list[0:end] 
print(new_list) #[] 
print (my_list[:len(my_list)]) #[10, 8, 6, 4, 2]

##############################################
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #[10, 4, 2]


##############################################
#eliminamos todos los elementos
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)  #[]
"""
El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) 
está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el operador devuelve
True en este caso.

El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) e
stá ausente en una lista - el operador devuelve True en este caso.
"""

my_list = [0, 3, 12, 8, 2]

print(5 in my_list) #false
print(5 not in my_list) #true
print(12 in my_list) #true

##############################################
my_list = [17, 3, 11, 45, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

##############################################
my_list = [12, 3, 11, 5, 1, 98, 7, 15, 13]
largest = my_list[0]
#print(my_list[1:]) #[3, 11, 5, 1, 9, 7, 15, 13]
print(largest)
for i in my_list[4:]:
    if i > largest:
        largest = i


##############################################
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 12
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


##############################################

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)


##############################################

vehicles_one = ['coche', 'bicicleta', 'motor']
print(vehicles_one) # output: ['coche', 'bicicleta', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # elimina 'coche'
print(vehicles_two) # output: ['bicicleta', 'motor']

##############################################

colors = ['rojo', 'verde', 'naranja']
 
copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista

##############################################
#También puede utilizar índices negativos para hacer uso de rebanadas. Por ejemplo:

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # output: ['C', 'D']

##############################################

#Los parámetros start y end son opcionales al partir
#en rebanadas una lista: list[start:end], por ejemplo:

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  # output: [3, 4, 5]
print(slice_two)  # output: [1, 2]
print(slice_three)  # output: [4, 5]

##############################################
#Puedes eliminar rebanadas utilizando la instrucción del:

my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # output: [3, 4, 5]
 
del my_list[:]
print(my_list)  # elimina el contenido de la lista, genera: []

##############################################
#Puedes probar si algunos elementos existen en una lista
#o no utilizando las palabras clave in y not in, por ejemplo:

my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # output: True
print("C" not in my_list)  # output: True
print(2 not in my_list)  # output: False

##############################################

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[0] 
 
print(list_3)

##############################################

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[:]
 
print(list_3)

##############################################

list_1 = ["A", "B", "C"]
list_2 = list_1[0:1]
list_3 = list_1[:]
 
del list_1[0]
del list_2[0]
 
print(list_3)
'''
##############################################
my_list = [1, 2, "in", True, "ABC"]
 
print(1 in my_list)  # output True
print("A" not in my_list)  # output True
print(3 not in my_list)  # output True
print(False in my_list)  # output False
 