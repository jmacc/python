#list
print("Lists")
my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

my_list = [12,34,567,89]
print(my_list)
print("Longitud de la lista")
print(len(my_list))

my_other_list = [34,56,4,"Jose","Bien",56,89,45,23]
print("Tipo de dato")
print(type(my_other_list))

print("Obtener datos en cierto orden")
print(my_other_list[1])
print(my_other_list[0])
print(my_other_list[-1])
#print(my_other_list[-5])#IndexError

#reordenamiento de lista en reversa
my_other_list.reverse()
print(my_other_list)

print("Append")
my_other_list.append("perico")
print(my_other_list)

print("Insert")
my_other_list.insert(1,"insertando")
print(my_other_list)

''' 
print("Remove")
my_other_list.remove((1)) #generar el error
print(my_other_list)
'''
#Elimina un valor conocido
print("Remove 2")
my_other_list.remove("insertando")
print(my_other_list)

print("Pop")
my_other_list.pop()
print(my_other_list)

#Elimina por indice
del my_other_list[1]





