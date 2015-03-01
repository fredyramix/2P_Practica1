# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import os
def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def menu():
    funciones={'1':'x^2','2':'sin x * 40','3':'(1000/abs(50-x))+x','4':'operacion4','5':'operacion5'}
    print"\t\tInstituto Politecnico Nacional"
    print "\t\tEscuela Superior de Computo"
    print "\t\tArtificial Intelligence"
    print "\t\tRamirez Ramirez Jesus Alfredo"
    print "\t\tAnguiano Mendoza Alan Gerardo"
    print "\t\tGrupo: 3CV3"
    print "\t\t2 Parcial practica 1"
    print "Selecciona una opcion:"
    print "[1].-F(x)=x^2"
    print "[2].-F(x)=sin x * 40"
    print "[3].-F(x)=(1000/abs(50-x))+x"
    print "[4].-F(x)=(1000/abs(50-x))+x"
    print "[5].-F(x)=((1000/abs(30-x))+(1000/abs(50-x))+(1000/abs(80-x)))+x"
    x=input("Ingresa una opcion: ")



    if funciones.has_key(str(x)):
        variables=[]
        variables.append(str(x))
        variables.append(raw_input("Ingrese el numero de cromosomas: "))
        variables.append(raw_input("Ingrese el numero de generaciones: "))
        print "Ingrese Rango X: 0<=X<=200"
        variables.append(raw_input("Minimo de X:"))
        variables.append(raw_input("Maximo de X:"))
        variables.append(raw_input("Max [1] o Min [0] :"))
        return(variables)
    else:
        print "Error opción no encontrada"
        cls()
        menu()



