#3.7.1 Listas dentro de listas
'''
#row = [WHITE_PAWN for i in range(8)]
##############################################


squares = [x ** 2 for x in range(10)] #el mimos valor multiplicado 2 veces dentro del rango 1 al 10
print(squares)
##############################################

twos = [2 ** i for i in range(8)]
print(twos)

##############################################
odds = [x for x in squares if x % 2 != 0 ] #crea una lista con elementos impares
print(odds)

##############################################

#3.7.2 Arreglos de dos dimensiones
board = [[EMPTY for i in range(8)] for j in range(8)]
#La parte interna crea una fila, y la parte externa crea una lista de filas.

##############################################
#TABLERO DE AJEDREZ
WHITE_SQUARE = 0
BLACK_SQUARE = 1
BLACK_CHESS_KNIGHT = #"\U0000265E"
BLACK_CHESS_PAWN = #"\U0000265F"

def print_row(row):
    for square in row:
        if square == WHITE_SQUARE:
            print(BLACK_CHESS_KNIGHT, end=" ")
        else:
            print(BLACK_CHESS_PAWN, end=" ")
        print("|", end=" ")
    print()

board = [[WHITE_SQUARE if (i+j)%2 == 0 else BLACK_SQUARE for i in range(8)] for j in range(8)]

for i in range(8):
    print_row(board[i])
    if i != 7:
        print("--+---+---+---+---+---+---+---+")

##############################################
#

board = []
board2 = [["x","x", "x"], ["x", "x", "x"]]
for i in range(3):
    #row = "x"
    #row = ["x" for j in range(4)]
    #board.append(row)
    #print(board)
    #row[0][0]=2
    #print(row)
    board2[0][0]=2
    board2[1][1]=4
    #board[2][2]=6
    #board[0][3]=8
    print(board2)
    
    #print(i)

##############################################
a = [[1, 2, 3], [4, 5, 6]]
#print(a[0])
#print(a[1])
b = a[0]
#b = a
#print(b)
#print(a[0][2])
a[0][1] = 7
#print(a)
#print(b)
b[2] = 9
print(b)
print(a[1])


##############################################
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
    

##############################################   
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=" ")
    print()

##############################################    
#Así es como puede usar 2 bucles anidados para calcular 
#la suma de todos los números en la lista bidimensional:
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)

##############################################  
# 
#Cubo - un arreglo tridimensional (3x3x3) 
cube = [[[':(', 'x', 'x'], [':)', 'x', 'x'], [':(', 'x', 'x']],
        [[':)', 'x', 'x'], [':(', 'x', 'x'], [':)', 'x', 'x']],
        [[':(', 'x', 'x'], [':)', 'x', 'x'], [':)', 'x', 'x']]]
print(cube)
print(cube[0][0][0]) # output: ':(' 
print(cube[2][2][0]) # output: ':)'

##############################################  
x = 1
x = x == x
print(x)

############################################## 
i = 0
while i <= 3 :
    i += 2
    print("*")

##############################################  
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

##############################################
for i in range(1):
    print("#")
else:
    print("#")

##############################################
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

##############################################  
var = 1
while var < 10:
    #print("#")
    print(var)
    var = var << 1
    print(var)

##############################################  
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

##############################################
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
 
print(c + d + e)

##############################################
my_list = [3, 1, -2]
print(my_list[my_list[-1]])

##############################################
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

##############################################
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

##############################################
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

##############################################
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(vals)

##############################################
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

##############################################
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

##############################################
my_list = [i for i in range(-1, 2)]
print(my_list)

##############################################
t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
'''
##############################################
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])