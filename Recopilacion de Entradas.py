#Recopilacion de Entradas
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print("1"+2)
#print(sys.argv[1]) # first arg
'''
Limpieza de paquetes no utilizados
A veces, es posible que se dé cuenta de que ya no necesita un determinado paquete de Python
y, por tanto, desea quitarlo. En ese caso, puede usar : pip uninstall python-dateutil
'''

'''
Para borrar todo lo que dependía de este paquete, puede escribir 
todos los paquetes instalados en una lista derequirements.txt, de la siguiente manera:
pip freeze > requirements.txt

A continuación, quite todos los paquetes de esa lista, de la siguiente manera:
pip uninstall -r requirements.txt -y
'''
