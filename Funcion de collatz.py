#Funcion de collatz en forma basica coomo una funcion
#ejercio https://www.youtube.com/watch?v=s8D-cYxOno0
#Python - Nivel 18 - Reto 16 - Conjetura de Collatz

def collatz(num):
    sec =[num]
    while num > 1:
        if num %2 == 0:
            num //= 2
        else:
            num =num*3+1
        sec.append(num)
    return sec

#pasamos valores
secuencia = collatz(5)

for i in secuencia:
    print(i, end=" ")