print(1,2,3,4,5)
print(1,2,3,4,5, sep=",", end=".")

my_string_variable ="La primera varaible"
print(my_string_variable)

my_init_variable = 5
print(my_init_variable)

my_init_to_str_variable =str(my_init_variable)
print(my_init_to_str_variable)
print(type(my_init_to_str_variable)) #indica el tipo de dato

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables de un print
print(my_init_variable,my_init_to_str_variable,my_bool_variable)

#funciones del sistema
print(len(my_string_variable))

#variables en una sola linea
name, subname, alias, edad  = "Jorge","Castillo","Perico",35
print("Mi llamo",name,"Mi apellido es",subname,"Tengo la edad de ",edad,"años y me dicen",alias)

#imputs

name = input ("Hola, como te llamas?")
age = input("¡Cuantos años tienes?")

print (name)
print (age)

#formateo
name1, surname1, age1 = "Jose","Mario",12
print("Mi nombre es {} {} y mi edad es {}".format(surname1,name1,age1))
print("Mi nombre es %s %s y mi edad es %d " %(surname1,name1,age1))

