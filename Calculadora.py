#Calculadora

print("Bienvenido a la calculadora")
print("Realizada en Python")
print("*****************************")
print("Para realizar alguna operacion ingresa la opcion ")
print("1.- Multiplicacion")
print("2.- Suma")
print("3.- Resta")
print("4.- Division")
print("5.- Comparacion")
print("6.- Diferencia")
print("7.- Salir")

fin =False

while not (fin):
    opc=int(input("Ingresa una Opcion  "))
    
    if (opc == 1): #Multiplicacion
        mul1 = float(input("ingresa el primer valor "))
        mul2 = float(input("ingresa el segundo valor "))
        print("El resultado es: ",mul1*mul2)
    
    elif (opc == 2): #Suma
        sum1 = float(input("ingresa el primer valor "))
        sum2 = float(input("ingresa el segundo valor "))
        print("El resultado es: ",sum1+sum2)
    
    elif (opc == 3): #Resta
        rest1 = float(input("ingresa el primer valor "))
        rest2 = float(input("ingresa el segundo valor "))
        print("El resultado es: ",rest1-rest2)
    
    elif (opc == 4): #Division
        div1 = float(input("ingresa el primer valor "))
        div2 = float(input("ingresa el segundo valor "))
        print("El resultado es: ",div1-div2)
        
    elif (opc == 5): #Comparacion
        com1 = float(input("ingresa el primer valor "))
        com2 = float(input("ingresa el segundo valor "))
        if com1 > com2:
            print("El varlo1: "+str(com1)+" es mayor a valor2: ",str(com2))
        else:
            print("El varlo1: "+str(com1)+" es menor a valor2: ",str(com2))
        
    elif (opc == 6): #Diferencia
        dif1 = float(input("ingresa el primer valor "))
        dif2 = float(input("ingresa el segundo valor "))
        if dif1 == dif2:
            print("El varlo1: "+str(dif1)+" es igual a valor2: ",str(dif2))
        else:
            print("El varlo1: "+str(dif1)+" es diferente a valor2: ",str(dif2))
    elif (opc == 7): #Sale de codigo
        print("Bye")
        fin = True