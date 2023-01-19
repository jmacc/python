#Bucles

#While
"""
dia = 0    
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo','Terminator']
while dia < 4:
   print("Hoy es " + semana[dia])
   dia += 1
"""
#-------------------------------------------------
"""
num = 0
while num < 10:
    print(num,end=" ")
    num += 1
"""
#-------------------------------------------------
"""
datos = True
while datos:
    valor = int(input("Ingresa un valor mayor a 10 "))
    if valor > 10:
        datos = False
    print("Programa Finalizado")

#------------------------------------------------------    
#For
lista =[1,2,3,4,"casa","coche","avion"]
for item in lista:
    print(lista)

#-------------------------------------------------   
for item in range(15):
    print(item)
"""
for item2 in range(3):
    for item3 in range(5):
        print("item2: "+str(item2)+" item3: "+str(item3))
        
""""        
dato1 = 0
while dato1 < 3:  
    for dato2 in range(5):
        print("item1: "+str(dato1)+" item2: "+str(dato2))
        #print("item2: "+str(dato2))
        #print("item1: "+str(dato1))
        dato1 = dato1 +1
"""