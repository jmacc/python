#3.5.2 Ordenando una lista - CiscoSkill
############################################
"""
my_list = [8,10,7,6,5,4,1]
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
############################################

my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)
############################################

lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst) #A,D,F,Z
############################################

a = 3
b = 1
c = 2
 
lst = [a, c, b]
lst.sort()
 
print(lst) #[1, 2, 3]
############################################
"""
a = "A"
b = "B"
c = "C"
d = " "
 
lst = [a, b, c, d]
lst.reverse()
 
print(lst)#[' ', 'C', 'B', 'A']