# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import  *
from menus import *
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
    resultado=primera_generacion(variables)
    #Despues de la primera generacion viene el ciclo hasta el numero de generaciones.
    #print resultado
    #ImprimeGeneracion(resultado)
    funciones_evaluadas=Calculo_fx(resultado)
    #Siguiente paso l penalizacion a los individuos que su codificacion salgan del rango de X
    #Calcular la probabilidad de ser elegidos.
    #print(funciones_evaluadas)
    cromos=Penalizar(funciones_evaluadas,variables)
    ImprimePenalizacion(cromos)
    #Calcular la probabilidad de ser elegidos en base a su penalizacion y si es maximo o  minimo.
    sumatoria=SumatoriaFX(cromos)
    #asignar probabilidad de ser elegido.
    lista_con_probabilidad=Probabilidad(sumatoria,cromos)
    ImprimeProbabilidad(lista_con_probabilidad)
    opciones_disponibles=Ruleta(lista_con_probabilidad)
    # print opciones_disponibles
    # raw_input("espera")
    parejas=SeleccionParejas(opciones_disponibles,variables)
    ImprimeParejas(parejas)


main()
