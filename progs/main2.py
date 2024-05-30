from sys import path
import os

path.append('c:\\Users\\AdministracionRed\\Documents\\Python Ejercicios\\packages')
#path.append(os.path.join(os.path.dirname(__file__), '..', 'c:\Users\AdministracionRed\Documents\Python Ejercicios\packages\extra'))

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT
 
print(extra.good.best.sigma.FunS())
print(FunT())