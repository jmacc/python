#3.4.2 Indexación de listas
##############################################
"""
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.
##############################################
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
 
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.


print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.
print(numbers[3])

del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[-3]) #a partir del ultimo de la lista

##############################################

dato = 0
rabbit=[1,2,3,4,5]
while dato <= 5:
    number=int(input("Que dijito quieres remplazar 1,2,3,4,5: "))
    new_number=input("Ingresa el nuevo digito: ")
    rabbit.remove(number) #eliminar el valor ingresado
    rabbit.append(new_number) #agrega el nuevo valor a la lista
    print(rabbit) #imprime la nueva lista
##############################################

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

##############################################

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1) #agrega un elemento a la ultima posicion

print(my_list)
##############################################

my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1) #agregar el numero a la primera posicion
 
print(my_list)
##############################################

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
##############################################

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i
 
print(total)
##############################################

'''
Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas.
Tu tarea es:

paso 1: crea una lista vacía llamada beatles;
paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.
Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?)
'''
# paso 1
beatles = []
beatles_add = ["John Lennon", "Paul McCartney "," George Harrison"]
paso_3_0 = "Stu Sutcliffe"
paso_3_1 ="Pete Best"
paso_3_2 ="Ringo Starr"
print("Paso 1:", beatles)
beatles.extend(beatles_add) #nos permite agrupar listas
print("Paso 2:", beatles)
for name in ["Stu Sutcliffe", "Pete Best"]:
    add = input("¿Deseas agregar a {}? s/n: ".format(name))
    if add == "s":
        beatles.append(name)
        print("La lista queda asi:", beatles)
    else:
        print("La lista queda asi:", beatles)
print("Eliminamos los Siguientes elementos  Stu Sutcliffe y Pete Best")
beatles.remove(paso_3_0)
beatles.remove(paso_3_1)
print("Al eliminar queda asi:", beatles)
beatles.insert(0,paso_3_2)
print("Al insertar al principio de las lista queda asi:", beatles)
##############################################

my_list = [1, None, True, 'Soy una cadena', 256, 0]
print(my_list[3])  # output: Soy una cadena
print(my_list[-1])  # output: 0
 
my_list[1] = '?'
print(my_list)  # output: [1, '?', True, 'Soy una cadena', 256, 0]
 
my_list.insert(0, "primero")
my_list.append("último")
print(my_list)  # output: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']

##############################################

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # output: [1, 2, 4]
 
del my_list  # borra la lista entera

##############################################

my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
 
for color in my_list:
    print(color)

##############################################
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(my_list))  # output 5
 
del my_list[2]
print(len(my_list))  # output 4

##############################################
"""
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))