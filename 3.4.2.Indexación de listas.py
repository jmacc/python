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
"""
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i
 
print(total)