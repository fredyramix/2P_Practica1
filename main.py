# -*- encoding: utf-8 -*-
from lista_funciones import EvaluarConElite
from mutacion import Mutacion

__author__ = 'fredy'
from funciones import  *
from menus import *
from cruzamiento import *
import os

#definición de cromosoma:
# x = [, , , , , ]
#combinaciones entre 1 y 0 maximo 31
#F(x)= x^2 donde  donde  0>=x<=31

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def main():
    cls()
    variables=menu()
    print "Primera Generacion Aleatoria"
    resultado=primera_generacion(variables)
    ImprimePrimeraGeneracion(resultado)
    #Despues de la primera generacion viene el ciclo hasta el numero de generaciones.
    #print resultado
    #ImprimeGeneracion(resultado)
    x=1
    best=[]

    print "Realizando algoritmo genetico esto puede llevar algunos minutos por favor espere..."
    while x!=int(variables[2]):
        funciones_evaluadas=Calculo_fx(resultado)
        #Siguiente paso l penalizacion a los individuos que su codificacion salgan del rango de X
        #Calcular la probabilidad de ser elegidos.
        #print(funciones_evaluadas)
        cromos=Penalizar(funciones_evaluadas,variables)
        #ImprimePenalizacion(cromos)
        #Calcular la probabilidad de ser elegidos en base a su penalizacion y si es maximo o  minimo.
        sumatoria=SumatoriaFX(cromos)
        #print(sumatoria)
        #asignar probabilidad de ser elegido.
        lista_con_probabilidad=Probabilidad(sumatoria,cromos,variables)
        #ImprimeProbabilidad(lista_con_probabilidad)
        opciones_disponibles=Ruleta(lista_con_probabilidad)
        # print opciones_disponibles
        # raw_input("espera")
        padres,hijos=SeleccionParejas(opciones_disponibles,variables)

        #dict=GenerarLlaves(cromosomas_cruzados)
        dict1=GenerarLlaves(hijos)
        best666=EvaluarConElite(dict1,variables,best)
        best=best666[:]

        #Apartir de aqui comienza el cruzamiento.
        cromosomas_cruzados=Cruzar(hijos,variables)
        #Apartir de este punto sigue la mutacion.
        nueva_generacion=Mutacion(cromosomas_cruzados)
        #print nueva_generacion
        dict1=GenerarLlaves(nueva_generacion)
        #best666=EvaluarConElite(dict,variables,best)
        #best=best666[:]
        resultado=dict1
        x=x+1
    print "Acabo en numero de generacion= " + str(x)
    print("El resultado final es: \n")
    print "X= " + str(best[1])
    print "F(x)= " + str(best[0])


main()
