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

'''
##############################################
#eliminamos todos los elementos
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)  #[]

