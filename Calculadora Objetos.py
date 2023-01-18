#Calculadora Objetos

def Multiplica():
    dato1 = float(input("ingresa el primer valor "))
    dato2 = float(input("ingresa el segundo valor "))
    print("El resultado de la multiplicacion es: ",dato1*dato2)
    Menu()
    Calculadora()

def Suma():
    dato1 = float(input("ingresa el primer valor "))
    dato2 = float(input("ingresa el segundo valor "))
    print("El resultado de la suma es: ",dato1+dato2)
    Menu()
    Calculadora()

def Resta():
    dato1 = float(input("ingresa el primer valor "))
    dato2 = float(input("ingresa el segundo valor "))
    print("El resultado de la resta es: ",dato1-dato2)
    Menu()
    Calculadora()
    
def Division():
    dato1 = float(input("ingresa el primer valor "))
    dato2 = float(input("ingresa el segundo valor "))
    print("El resultado de la division es: ",dato1/dato2)
    Menu()
    Calculadora()
    
def Comparacion():
    com1 = float(input("ingresa el primer valor "))
    com2 = float(input("ingresa el segundo valor "))
    if com1 > com2:
            print("El varlo1: "+str(com1)+" es mayor a valor2: ",str(com2))
            Menu()
            Calculadora()
    else:
            print("El varlo1: "+str(com1)+" es menor a valor2: ",str(com2))
            Menu()
            Calculadora()
    
def Diferencia():
    dif1 = float(input("ingresa el primer valor "))
    dif2 = float(input("ingresa el segundo valor "))
    if dif1 == dif2:
            print("El varlo1: "+str(dif1)+" es igual a valor2: ",str(dif2))
            Menu()
            Calculadora()
    else:
            print("El varlo1: "+str(dif1)+" es diferente a valor2: ",str(dif2))
            Menu()
            Calculadora()

def Calculadora():
    while True:
        try:
            opc=int(input("Ingresa una Opcion  "))
            fin =False
            while not (fin):
                if (opc == 1): #Multiplicacion
                    Multiplica()
                    continue
                elif (opc == 2): #Suma
                    Suma()
                    continue
                elif (opc == 3): #Resta
                    Resta()
                    continue
                elif (opc == 4): #Division
                    Division()
                    continue
                elif (opc == 5): #Comparacion
                    Comparacion()
                    continue
                elif (opc == 6): #Diferencia
                    Diferencia()
                    continue
                else: #Sale de codigo
                    print("No existe la opcion")
                    fin = True  
        except ValueError:
            print("Ingresa un valor del menu")
 
def Menu():               
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

Menu()
Calculadora()