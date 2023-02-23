## Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (12,34,6,7,8,6,45,"Perico","Avion","Lineas")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#Identifica si existe el dato
print(my_tuple.count("Perico"))
#Identifica su posicion
print(my_tuple.index("Lineas"))