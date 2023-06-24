#4.6 Sección 6 – Tuplas y diccionarios
##############################################
'''
La segunda noción
la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe 
su disponibilidad para poder cambiar 
libremente durante la ejecución de un programa. Existen dos tipos de datos 
en Python: mutables e inmutables.
Los datos mutables pueden ser actualizados libremente en cualquier momento
- a esta operación se le denomina "in situ".
''' 
##############################################
'''
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
print(tuple_1)
print(tuple_2)
##############################################

my_tuple = (1, 10, 100, 1000)
#my_tuple.append(10000) #no se puede modificar la tupla
del my_tuple[0]
my_tuple[1] = -10
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print("Lista 1 ->",my_tuple[0])
print("Lista 2 ->",my_tuple[-1])
print("Lista 3 ->",my_tuple[1:])
print("Lista 4 ->",my_tuple[:-2])
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


for elem in my_tuple:
    print("For ->",elem)
    
##############################################

#Diccionarios
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
##############################################

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
 ##############################################
   
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
#for key in sorted(dictionary.keys()): //lista ordenada
    print(key, "->", dictionary[key])
##############################################
  
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
print(dictionary)
dictionary['gato'] = 'minou'
dictionary.update({"pato": "canard"})
del dictionary['perro'] #elimina un elemento
dictionary.popitem() #elimina el ultimo elemento de la lista
for spanish, french in dictionary.items():
    print(spanish, "->", french)
##############################################

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
##############################################

my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)
##############################################
 
#tuplas de un solo elemento
#Si se elimina la coma, Python creará una variable no una tupla:
one_elem_tuple_1 = ("uno", ) # Paréntesis y una coma.
one_elem_tuple_2 = "uno", # Sin paréntesis, solo la coma

my_tuple_1 = 1,
print(type(my_tuple_1)) # salida: <class 'tuple'>
 
my_tuple_2 = 1 # Esto no es una tupla.
print(type(my_tuple_2)) # salida: <class 'int'>
##############################################

#Se pueden acceder los elementos de la tupla al indexarlos:
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(my_tuple[3]) # salida: [3, 4]
##############################################

my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
my_tuple[2] = "guitarra" # Se genera la excepción TypeError.
##############################################

#se puede eliminar la tupla completa:
my_tuple = 1, 2, 3,
del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined
##############################################

# Ejemplo 1-
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
 
# Ejemplo 2-verificar si un elemento o no esta presente
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
 
# Ejemplo 3-para verificar cuantos elementos existen en la tupla
tuple_2 = (1, 2, 3, 4)
print(len(tuple_2))
print(5 not in tuple_2)

# Ejemplo 4-incluso unir o multiplicar tuplas
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_2 * 2
 
print(tuple_4)
print(tuple_5)

##############################################

my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # salida: [2, 4, 6]
print(type(my_list)) # salida: <class 'list'>
tup = tuple(my_list)
print(tup) # salida: (2, 4, 6)
print(type(tup)) # salida: <class 'tuple'>
##############################################

tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # salida: <class 'list'>
##############################################

pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }
 
item_1 = pol_esp_dictionary["gleba"] # Ejemplo 1
print(item_1) # salida: tierra
 
item_2 = pol_esp_dictionary.get("woda") # Ejemplo 2
print(item_2) # salida: agua
##############################################

pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]
print(item) # salida: cerradura
##############################################

phonebook = {} # un diccionario vacío
 
phonebook["Adán"] = 3456783958 # crear/agregar un par clave-valor
print(phonebook) # salida: {'Adán': 3456783958}
 
del phonebook["Adán"]
print(phonebook) # salida: {}

##############################################

pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
print(len(pol_esp_dictionary)) # salida: 3
del pol_esp_dictionary["zamek"] # eliminar un elemento
print(len(pol_esp_dictionary)) # salida: 2
 
pol_esp_dictionary.clear() # eliminar todos los elementos
print(len(pol_esp_dictionary)) # salida: 0
 
del pol_esp_dictionary # elimina el diccionario
##############################################

pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
copy_dictionary = pol_esp_dictionary.copy()
##############################################

tup = 1, 2, 3
a, b, c = tup
 
print(a * b * c)
# Los elementos de la tupla tup han sido "desempaquetados" en las variables a, b, y c.
##############################################

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # salida: 4
##############################################
#nueva lista
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

##############################################

#lista a tupla

my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)
##############################################

#tupla a diccionario
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print("dicctionary->",colors_dictionary)
print("tupla->",colors)
##############################################

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
 
print(copy_my_dictionary)
##############################################
'''
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }
 
for col, rgb in colors.items():
    print(col, ":", rgb)