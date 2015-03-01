# -*- encoding: utf-8 -*-
__author__ = 'fredy'

#Archivo para funciones de cruzamiento.

def Cruzar(hijos,variables):
    cruzados=[]

    tamtotal=len(hijos) # tamaño de individuos
    tamtotalcromosoma=len(hijos[0]) #tamaño de bits
    mitad=tamtotalcromosoma/2
    while len(hijos)!=0:
        try:
            a=hijos[0]
            mitad1 = a[0:mitad]
            mitad2 = a[mitad:tamtotalcromosoma]
            b=hijos[1]
            mitad3 = b[0:mitad]
            mitad4 = b[mitad:tamtotalcromosoma]
            mitad1+=mitad4
            mitad3+=mitad2
            cruzados.append(mitad1)
            cruzados.append(mitad3)
            del hijos[0]
            del hijos[0]
        except IndexError,e:
            cruzados.append(a)
            break
    return cruzados