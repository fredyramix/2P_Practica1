# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random


def Mutacion(cromosomas_cruzados):
    tamtotal=len(cromosomas_cruzados) # tamaño de individuos
    tamtotalcromosoma=len(cromosomas_cruzados[0]) #tamaño de bits
    cromosoma_a_mutar=random.randrange(0,tamtotal)
    posicion_bit=random.randrange(0,tamtotalcromosoma)
    a=cromosomas_cruzados[cromosoma_a_mutar]
    #print cromosoma_a_mutar
    temp=[]
    for x in a:
        temp.append(x)
    if temp[posicion_bit]=='1':
        temp[posicion_bit]='0'
    else:
        temp[posicion_bit]='1'
    concat=""
    for y in temp:
        concat+=str(y)
    cromosomas_cruzados[cromosoma_a_mutar]=concat
    return cromosomas_cruzados